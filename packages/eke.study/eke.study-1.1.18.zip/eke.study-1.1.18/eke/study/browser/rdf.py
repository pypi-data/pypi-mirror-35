# encoding: utf-8
# Copyright 2009–2016 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''
EKE Studies: RDF ingest for study folders and their protocols.
'''

from Acquisition import aq_inner
from eke.knowledge.browser.rdf import IngestHandler, KnowledgeFolderIngestor, CreatedObject, RDFIngestException, Results
from eke.knowledge.browser.utils import updateObject
from eke.study import ProjectMessageFactory as _
from eke.study.interfaces import IProtocol
from plone.i18n.normalizer.interfaces import IIDNormalizer
from Products.CMFCore.utils import getToolByName
from rdflib import ConjunctiveGraph, URLInputSource, URIRef
from zope.component import queryUtility
from eke.study.utils import COLLABORATIVE_GROUP_DMCC_IDS_TO_NAMES
import logging, time, urlparse, os.path

_logger              = logging.getLogger(__name__)
_typeURI             = URIRef('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
_protocolTypeURI     = URIRef('http://edrn.nci.nih.gov/rdf/types.rdf#Protocol')
_siteSpecificTypeURI = URIRef('http://edrn.nci.nih.gov/rdf/types.rdf#ProtocolSiteSpecific')
_projectFlagURI      = URIRef('http://edrn.nci.nih.gov/rdf/schema.rdf#projectFlag')
_siteURIPrefix       = u'http://edrn.nci.nih.gov/data/sites/'

# Interface identifier for EDRN Collaborative Group, from edrnsite.collaborations
_collabGroup = 'edrnsite.collaborations.interfaces.collaborativegroupindex.ICollaborativeGroupIndex'


class StudyFolderIngestor(KnowledgeFolderIngestor):
    '''Study folder ingestion.'''
    def __call__(self, rdfDataSource=None):
        '''Ingest and render a results page'''
        context = aq_inner(self.context)
        _logger.info('Study Folder RDF ingest for folder at %s', '/'.join(context.getPhysicalPath()))
        catalog = getToolByName(context, 'portal_catalog')
        if rdfDataSource is None:
            rdfDataSource = context.rdfDataSource
        if not rdfDataSource:
            raise RDFIngestException(_(u'This folder has no RDF data source URL.'))
        normalizerFunction = queryUtility(IIDNormalizer).normalize
        t0 = time.time()
        graph = ConjunctiveGraph()
        graph.parse(URLInputSource(rdfDataSource))
        statements = self._parseRDF(graph)
        delta = time.time() - t0
        _logger.info('Took %f seconds to read and parse %s', delta, rdfDataSource)
        createdObjects = []
        handler = StudyHandler()
        t0 = time.time()
        # First gather the protocol-to-involved investigator sites
        protocolToInvolvedSites = {}
        for uri, predicates in statements.items():
            typeURI = predicates[_typeURI][0]
            if typeURI == _siteSpecificTypeURI:
                protocolID, siteID = os.path.basename(urlparse.urlparse(unicode(uri)).path).split(u'-')
                siteIDs = protocolToInvolvedSites.get(protocolID, set())
                siteIDs.add(siteID)
                protocolToInvolvedSites[protocolID] = siteIDs
        # Now go through each protocol
        for uri, predicates in statements.items():
            typeURI = predicates[_typeURI][0]
            if typeURI == _siteSpecificTypeURI: continue
            if unicode(uri) == u'http://edrn.nci.nih.gov/data/protocols/0':
                # Bad data from DMCC
                continue
            results = catalog(identifier=unicode(uri), object_provides=IProtocol.__identifier__)
            objectID = handler.generateID(uri, predicates, normalizerFunction)
            isProject = unicode(predicates.get(_projectFlagURI, ['Protocol'])[0]) == u'Project'
            if len(results) == 1 or objectID in context.keys():
                # Existing protocol. Update it.
                if objectID in context.keys():
                    p = context[objectID]
                else:
                    p = results[0].getObject()
                oldID = p.id
                updateObject(p, uri, predicates, context)
                p.project = True if isProject else False
                newID = handler.generateID(uri, predicates, normalizerFunction)
                if oldID != newID:
                    # Need to update the object ID too
                    p.setId(newID)
                # And set the involved investigator sites
                self.setInvolvedInvestigatorSites(catalog, p, protocolToInvolvedSites)
                created = [CreatedObject(p)]
            else:
                if len(results) > 1:
                    # More than one? WTF? Nuke 'em all.
                    context.manage_delObjects([p.id for p in results])
                # New protocol. Create it.
                title = handler.generateTitle(uri, predicates)
                created = handler.createObjects(objectID, title, uri, predicates, statements, context)
                for createdObject in created:
                    createdObject.obj.project = True if isProject else False
                    self.setInvolvedInvestigatorSites(catalog, createdObject.obj, protocolToInvolvedSites)
            for obj in created:
                obj.reindex()
            createdObjects.extend(created)
        _logger.info('Took %f seconds to process %d statements', time.time() - t0, len(statements))
        self.objects = createdObjects
        t0 = time.time()
        self.updateCollaborativeGroups(createdObjects, catalog)
        _logger.info('Took %f seconds to update collaborative groups', time.time() - t0)
        # Now add involved investigator sites to protocols
        self._results = Results(self.objects, warnings=[])
        return self.renderResults()
    def setInvolvedInvestigatorSites(self, catalog, protocol, protocolToInvolvedSites):
        protocol.setInvolvedInvestigatorSites([])
        protocolID = os.path.basename(urlparse.urlparse(protocol.identifier).path).split(u'-')[0]
        siteNumbers = protocolToInvolvedSites.get(protocolID, [])
        siteIDs = [_siteURIPrefix + i for i in siteNumbers]
        siteBrains = catalog(identifier=siteIDs, sort_on='sortable_title')
        protocol.setInvolvedInvestigatorSites([i['UID'] for i in siteBrains])
    def updateCollaborativeGroups(self, createdObjects, catalog):
        for protocol in [i.obj for i in createdObjects]:
            cbText = protocol.collaborativeGroupText
            if not cbText: continue
            cbText = cbText.strip()  # DMCC sometimes has a single space in their database
            for cbID in cbText.split(', '):
                cbName = COLLABORATIVE_GROUP_DMCC_IDS_TO_NAMES.get(cbID)
                if cbName:
                    for collabGroup in [i.getObject() for i in catalog(object_provides=_collabGroup, Title=cbName)]:
                        currentProjects, currentProtocols = collabGroup.getProjects(), collabGroup.getProtocols()
                        if protocol.project and protocol not in currentProjects:
                            currentProjects.append(protocol)
                        elif protocol.project and protocol in currentProtocols:
                            currentProtocols.remove(protocol)
                        elif not protocol.project and protocol not in currentProtocols:
                            currentProtocols.append(protocol)
                        elif not protocol.project and protocol in currentProjects:
                            currentProjects.remove(protocol)
                        collabGroup.setProjects(currentProjects)
                        collabGroup.setProtocols(currentProtocols)


class StudyHandler(IngestHandler):
    '''Handler for ``Protocol`` objects.'''
    def generateID(self, uri, predicates, normalizerFunction):
        return str(uri.split('/')[-1]) + '-' + super(StudyHandler, self).generateID(uri, predicates, normalizerFunction)
    def createObjects(self, objectID, title, uri, predicates, statements, context):
        p = context[context.invokeFactory('Protocol', objectID)]
        updateObject(p, uri, predicates, context)
        return [CreatedObject(p)]
