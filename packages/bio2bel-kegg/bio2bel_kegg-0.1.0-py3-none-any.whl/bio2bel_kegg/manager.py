# -*- coding: utf-8 -*-

"""Manager for Bio2BEL KEGG."""

import json
import logging
import os
from multiprocessing.pool import ThreadPool

import bio2bel_hgnc
import requests
from bio2bel.manager.bel_manager import BELManagerMixin
from bio2bel.manager.flask_manager import FlaskMixin
from bio2bel.manager.namespace_manager import BELNamespaceManagerMixin
from compath_utils import CompathManager
from pybel.constants import BIOPROCESS, FUNCTION, NAME, NAMESPACE, PROTEIN
from pybel.manager.models import NamespaceEntry
from pybel.struct.graph import BELGraph
from tqdm import tqdm

from .constants import API_KEGG_GET, KEGG, METADATA_FILE_PATH, MODULE_NAME, PROTEIN_ENTRY_DIR
from .models import Base, Pathway, Protein
from .parsers import *

__all__ = [
    'Manager'
]

log = logging.getLogger(__name__)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class Manager(CompathManager, BELNamespaceManagerMixin, BELManagerMixin, FlaskMixin, ):
    """Manage the Bio2BEL KEGG database."""

    module_name = MODULE_NAME
    flask_admin_models = [Pathway, Protein]
    namespace_model = pathway_model = Pathway
    protein_model = Protein
    pathway_model_identifier_column = Pathway.kegg_id

    @property
    def _base(self):
        return Base

    def get_or_create_pathway(self, kegg_id, name=None):
        """Get an pathway from the database or creates it.

        :param str kegg_id: kegg identifier
        :param Optional[str] name: name of the pathway
        :rtype: Pathway
        """
        pathway = self.get_pathway_by_id(kegg_id)

        if pathway is None:
            pathway = Pathway(
                kegg_id=kegg_id,
                name=name
            )
            self.session.add(pathway)

        return pathway

    def get_protein_by_kegg_id(self, kegg_id):
        """Get a protein by its kegg id.

        :param kegg_id: kegg identifier
        :rtype: Optional[Protein]
        """
        return self.session.query(Protein).filter(Protein.kegg_id == kegg_id).one_or_none()

    def get_protein_by_hgnc_id(self, hgnc_id):
        """Get a protein by its hgnc_id.

        :param hgnc_id: hgnc_id
        :rtype: Optional[Protein]
        """
        return self.session.query(Protein).filter(Protein.hgnc_id == hgnc_id).one_or_none()

    def get_protein_by_hgnc_symbol(self, hgnc_symbol):
        """Get a protein by its hgnc symbol.

        :param hgnc_id: hgnc identifier
        :rtype: Optional[Protein]
        """
        return self.session.query(Protein).filter(Protein.hgnc_symbol == hgnc_symbol).one_or_none()

    """Methods to populate the DB"""

    @staticmethod
    def _get_identifier(model):
        return model.kegg_id

    def _create_namespace_entry_from_model(self, model, namespace):
        """Create a namespace entry from a KEGG pathway model.

        :param Pathway model:
        :param pybel.manager.models.Namespace namespace:
        :rtype: NamespaceEntry
        """
        return NamespaceEntry(
            name=model.name,
            identifier=model.kegg_id,
            namespace=namespace,
            encoding='B',
        )

    def _populate_pathways(self, url=None):
        """Populate pathways.

        :param Optional[str] url: url from pathway table file
        """
        df = get_pathway_names_df(url=url)

        pathways_dict = parse_pathways(df)

        for kegg_id, name in tqdm(pathways_dict.items(), desc='Loading pathways'):
            self.get_or_create_pathway(kegg_id=kegg_id, name=name)

        self.session.commit()

    def _pathway_entity(self, url=None, metadata_existing=None, thead_pool_size=1):
        """Populate proteins.

        :param Optional[str] url: url from protein to pathway file
        :param Optional[bool] metadata_existing: metadata exists already
        """
        protein_df = get_entity_pathway_df(url=url)

        log.debug('creating description URLs')
        protein_description_entities = {
            entity
            for line, (entity, pathway) in protein_df.iterrows()
        }

        if not metadata_existing:
            # KEGG protein ID to Protein model attributes dictionary
            pid_attributes = {}

            log.info('Fetching all protein meta-information (needs around 7300 iterations).'
                     'You can modify the numbers of request by modifying ThreadPool to make this faster. '
                     'However, the KEGG RESTful API might reject a big amount of requests.')

            # Multi-thread processing of protein description requests
            results = ThreadPool(thead_pool_size).imap_unordered(self._process_kegg_api_get_entity,
                                                                 protein_description_entities)
            pid_attributes = dict(tqdm(results, desc='Fetching meta information'))
            self._postprocess_pid(pid_attributes)

            with open(METADATA_FILE_PATH, 'w') as outfile:
                json.dump(pid_attributes, outfile)

        else:
            log.info('Loading existing metadata file')
            pid_attributes = json.load(open(METADATA_FILE_PATH))

        log.info('Done fetching')

        pid_protein = {}

        for kegg_protein_id, kegg_pathway_id in tqdm(parse_entity_pathway(protein_df), desc='Loading proteins'):

            if kegg_protein_id in pid_protein:
                protein = pid_protein[kegg_protein_id]
            else:
                try:
                    protein = Protein(**pid_attributes[kegg_protein_id])
                except KeyError:
                    log.error('Protein key not found. This might be due to an old cached metadata file. '
                              'Please delete the file {} and try again.'.format(METADATA_FILE_PATH))
                    raise

                pid_protein[kegg_protein_id] = protein
                self.session.add(protein)

            pathway = self.get_pathway_by_id(kegg_pathway_id)
            protein.pathways.append(pathway)
        self.session.commit()

    @staticmethod
    def _process_kegg_api_get_entity(entity):
        """Send a given entity to the KEGG API and process the results.

        :param str entity: A KEGG identifier
        :return: A 2-tuple of the input value and the JSON retrieved from the API
        :rtype: tuple[str,dict]
        """
        _protein_path = os.path.join(PROTEIN_ENTRY_DIR, '{}.json'.format(entity))

        if os.path.exists(_protein_path):
            with open(_protein_path) as f:
                return entity, json.load(f)

        url = API_KEGG_GET.format(entity)
        result = requests.get(url)

        protein_dict = process_protein_info_to_model(result)
        protein_dict['kegg_id'] = entity

        with open(_protein_path, 'w') as f:
            json.dump(protein_dict, f)

        return entity, protein_dict

    def _postprocess_pid(self, pid_attributes):
        """Enrich the dictionary of KEGG API results with HGNC information."""
        hgnc_manager = bio2bel_hgnc.Manager(connection=self.connection)
        if not hgnc_manager.is_populated():
            hgnc_manager.populate()
        hgnc_id_to_symbol = hgnc_manager.build_hgnc_id_symbol_mapping()

        for kegg_protein_id in pid_attributes:

            hgnc_id = pid_attributes[kegg_protein_id].get('hgnc_id')
            if hgnc_id is not None:
                pid_attributes[kegg_protein_id]['hgnc_symbol'] = hgnc_id_to_symbol.get(hgnc_id)

    def populate(self, pathways_url=None, protein_pathway_url=None, metadata_existing=False):
        """Populate all tables."""
        self._populate_pathways(url=pathways_url)
        self._pathway_entity(url=protein_pathway_url, metadata_existing=metadata_existing)

    def count_pathways(self) -> int:
        """Count the pathways in the database."""
        return self._count_model(Pathway)

    def list_pathways(self):
        """List the pathways in the database.

        :rtype: list[Pathway]
        """
        return self._list_model(Pathway)

    def count_proteins(self) -> int:
        """Count the pathways in the database."""
        return self._count_model(Protein)

    def summarize(self):
        """Summarize the database.

        :rtype: dict[str,int]
        """
        return dict(
            pathways=self.count_pathways(),
            proteins=self.count_proteins(),
        )

    def to_bel(self):
        """Serialize KEGG to BEL.

        :rtype:
        """
        graph = BELGraph(
            name='KEGG Pathway Definitions',
            version='1.0.0',
        )
        for pathway in self.list_pathways():
            self._add_pathway_to_graph(graph, pathway)
        return graph

    @staticmethod
    def _add_pathway_to_graph(graph, pathway):
        pathway_node = pathway.serialize_to_pathway_node()

        for protein in pathway.proteins:
            graph.add_part_of(protein.serialize_to_protein_node(), pathway_node)

    def get_pathway_graph(self, kegg_id):
        """Return a new graph corresponding to the pathway.

        :param str kegg_id: A KEGG pathway identifier (prefixed by "path:")
        :rtype: Optional[pybel.BELGraph]
        """
        pathway = self.get_pathway_by_id(kegg_id)
        if pathway is None:
            return

        graph = BELGraph(
            name='{} graph'.format(pathway.name),
        )
        self._add_pathway_to_graph(graph, pathway)
        return graph

    def enrich_kegg_pathway(self, graph):
        """Enrich all proteins belonging to kegg pathway nodes in the graph.

        :param pybel.BELGraph graph: A BEL Graph
        """
        for node, data in graph.nodes(data=True):
            if data[FUNCTION] == BIOPROCESS and data[NAMESPACE] == KEGG and NAME in data:
                pathway = self.get_pathway_by_name(data[NAME])

                for protein in pathway.proteins:
                    graph.add_part_of(protein.serialize_to_protein_node(), node)

    def enrich_kegg_protein(self, graph):
        """Enrich all kegg pathways associated with proteins in the graph.

        :param pybel.BELGraph graph: A BEL Graph
        """
        for node, data in graph.nodes(data=True):
            if data[FUNCTION] == PROTEIN and data[NAMESPACE] == 'HGNC':
                protein = self.get_protein_by_hgnc_symbol(data[NAME])

                for pathway in protein.pathways:
                    graph.add_part_of(node, pathway.serialize_to_pathway_node())

    def _add_admin(self, app, **kwargs):
        from flask_admin import Admin
        from flask_admin.contrib.sqla import ModelView

        class PathwayView(ModelView):
            """Pathway view in Flask-admin"""
            column_searchable_list = (
                Pathway.kegg_id,
                Pathway.name
            )

        class ProteinView(ModelView):
            """Protein view in Flask-admin"""
            column_searchable_list = (
                Protein.kegg_id,
                Protein.uniprot_id,
                Protein.hgnc_id
            )

        admin = Admin(app, **kwargs)
        admin.add_view(PathwayView(Pathway, self.session))
        admin.add_view(ProteinView(Protein, self.session))
        return admin
