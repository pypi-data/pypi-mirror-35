# -*- coding: utf-8 -*-

import itertools as itt
from collections import Counter, defaultdict

import logging

from pybel.constants import *
from pybel.struct.filters import and_edge_predicates, concatenate_node_predicates, get_nodes_by_function
from pybel.struct.filters.edge_predicates import edge_has_annotation, is_causal_relation
from pybel.struct.filters.node_predicates import keep_node_permissive
from pybel.struct.pipeline import uni_in_place_transformation
from ..utils import safe_add_edge

__all__ = [
    'get_peripheral_successor_edges',
    'get_peripheral_predecessor_edges',
    'count_sources',
    'count_targets',
    'count_possible_successors',
    'count_possible_predecessors',
    'get_subgraph_edges',
    'get_subgraph_peripheral_nodes',
    'expand_periphery',
    'enrich_grouping',
    'enrich_complexes',
    'enrich_composites',
    'enrich_reactions',
    'enrich_variants',
    'enrich_unqualified',
    'expand_internal',
    'expand_internal_causal',
]

log = logging.getLogger(__name__)


def get_peripheral_successor_edges(graph, subgraph):
    """Gets the set of possible successor edges peripheral to the subgraph. The source nodes in this iterable are
    all inside the subgraph, while the targets are outside.

    :param pybel.BELGraph graph: A BEL graph
    :param subgraph: An iterator of BEL nodes
    :return: An iterable of possible successor edges (4-tuples of node, node, key, data)
    :rtype: iter[tuple]
    """
    for u in subgraph:
        for _, v, k, d in graph.out_edges_iter(u, keys=True, data=True):
            if v not in subgraph:
                yield u, v, k, d


def get_peripheral_predecessor_edges(graph, subgraph):
    """Gets the set of possible predecessor edges peripheral to the subgraph. The target nodes in this iterable
    are all inside the subgraph, while the sources are outside.

    :param pybel.BELGraph graph: A BEL graph
    :param subgraph: An iterator of BEL nodes
    :return: An iterable on possible predecessor edges (4-tuples of node, node, key, data)
    :rtype: iter[tuple]
    """
    for v in subgraph:
        for u, _, k, d in graph.in_edges_iter(v, keys=True, data=True):
            if u not in subgraph:
                yield u, v, k, d


def count_sources(edge_iter):
    """Counts the source nodes in an edge iterator with keys and data

    :param iter[tuple] edge_iter: An iterable on possible predecessor edges (4-tuples of node, node, key, data)
    :return: A counter of source nodes in the iterable
    :rtype: collections.Counter
    """
    return Counter(u for u, _, _, _ in edge_iter)


def count_targets(edge_iter):
    """Counts the target nodes in an edge iterator with keys and data

    :param iter[tuple] edge_iter: An iterable on possible predecessor edges (4-tuples of node, node, key, data)
    :return: A counter of target nodes in the iterable
    :rtype: collections.Counter
    """
    return Counter(v for _, v, _, _ in edge_iter)


def count_possible_successors(graph, subgraph):
    """

    :param pybel.BELGraph graph: A BEL graph
    :param subgraph: An iterator of BEL nodes
    :return: A counter of possible successor nodes
    :rtype: collections.Counter
    """
    return count_targets(get_peripheral_successor_edges(graph, subgraph))


def count_possible_predecessors(graph, subgraph):
    """

    :param pybel.BELGraph graph: A BEL graph
    :param subgraph: An iterator of BEL nodes
    :return: A counter of possible predecessor nodes
    :rtype: collections.Counter
    """
    return count_sources(get_peripheral_predecessor_edges(graph, subgraph))


def get_subgraph_edges(graph, annotation, value, source_filter=None, target_filter=None):
    """Gets all edges from a given subgraph whose source and target nodes pass all of the given filters

    :param pybel.BELGraph graph: A BEL graph
    :param str annotation:  The annotation to search
    :param str value: The annotation value to search by
    :param source_filter: Optional filter for source nodes (graph, node) -> bool
    :param target_filter: Optional filter for target nodes (graph, node) -> bool
    :return: An iterable of (source node, target node, key, data) for all edges that match the annotation/value and
             node filters
    :rtype: iter[tuple]
    """
    if source_filter is None:
        source_filter = keep_node_permissive

    if target_filter is None:
        target_filter = keep_node_permissive

    for u, v, k, data in graph.edges_iter(keys=True, data=True):
        if not edge_has_annotation(data, annotation):
            continue
        if data[ANNOTATIONS][annotation] == value and source_filter(graph, u) and target_filter(graph, v):
            yield u, v, k, data


def get_subgraph_peripheral_nodes(graph, subgraph, node_filters=None, edge_filters=None):
    """Gets a summary dictionary of all peripheral nodes to a given subgraph

    :param pybel.BELGraph graph: A BEL graph
    :param iter[tuple] subgraph: A set of nodes
    :param node_filters: Optional. A list of node filter predicates with the interface (graph, node) -> bool. See
                         :mod:`pybel_tools.filters.node_filters` for more information
    :type node_filters: lambda
    :param edge_filters: Optional. A list of edge filter predicates with the interface (graph, node, node, key, data)
                          -> bool. See :mod:`pybel_tools.filters.edge_filters` for more information
    :type edge_filters: lambda
    :return: A dictionary of {external node: {'successor': {internal node: list of (key, dict)},
                                            'predecessor': {internal node: list of (key, dict)}}}
    :rtype: dict

    For example, it might be useful to quantify the number of predecessors and successors

    >>> import pybel_tools as pbt
    >>> sgn = 'Blood vessel dilation subgraph'
    >>> sg = pbt.selection.get_subgraph_by_annotation_value(graph, annotation='Subgraph', value=sgn)
    >>> p = pbt.mutation.get_subgraph_peripheral_nodes(graph, sg, node_filters=pbt.filters.exclude_pathology_filter)
    >>> for node in sorted(p, key=lambda n: len(set(p[n]['successor']) | set(p[n]['predecessor'])), reverse=True):
    >>>     if 1 == len(p[sgn][node]['successor']) or 1 == len(p[sgn][node]['predecessor']):
    >>>         continue
    >>>     print(node,
    >>>           len(p[node]['successor']),
    >>>           len(p[node]['predecessor']),
    >>>           len(set(p[node]['successor']) | set(p[node]['predecessor'])))
    """
    node_filter = concatenate_node_predicates(node_predicates=node_filters)
    edge_filter = and_edge_predicates(edge_predicates=edge_filters)

    result = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    for u, v, k, d in get_peripheral_successor_edges(graph, subgraph):
        if not node_filter(graph, v) or not node_filter(graph, u) or not edge_filter(graph, u, v, k, d):
            continue
        result[v]['predecessor'][u].append((k, d))

    for u, v, k, d in get_peripheral_predecessor_edges(graph, subgraph):
        if not node_filter(graph, v) or not node_filter(graph, u) or not edge_filter(graph, u, v, k, d):
            continue
        result[u]['successor'][v].append((k, d))

    return result


@uni_in_place_transformation
def expand_periphery(universe, graph, node_filters=None, edge_filters=None, threshold=2):
    """Iterates over all possible edges, peripheral to a given subgraph, that could be added from the given graph.
    Edges could be added if they go to nodes that are involved in relationships that occur with more than the
    threshold (default 2) number of nodes in the subgraph.

    :param pybel.BELGraph universe: The universe of BEL knowledge
    :param pybel.BELGraph graph: The (sub)graph to expand
    :param node_filters: Optional. A list of node filter predicates with the interface (graph, node) -> bool. See
                         :mod:`pybel_tools.filters.node_filters` for more information
    :type node_filters: lambda
    :param edge_filters: Optional. A list of edge filter predicates with the interface (graph, node, node, key, data)
                          -> bool. See :mod:`pybel_tools.filters.edge_filters` for more information
    :type edge_filters: lambda
    :param threshold: Minimum frequency of betweenness occurrence to add a gap node

    A reasonable edge filter to use is :func:`pybel_tools.filters.keep_causal_edges` because this function can allow
    for huge expansions if there happen to be hub nodes.
    """
    nd = get_subgraph_peripheral_nodes(universe, graph, node_filters=node_filters, edge_filters=edge_filters)

    for node, dd in nd.items():
        pred_d = dd['predecessor']
        succ_d = dd['successor']

        in_subgraph_connections = set(pred_d) | set(succ_d)

        if threshold > len(in_subgraph_connections):
            continue

        graph.add_node(node, attr_dict=universe.node[node])

        for u, edges in pred_d.items():
            for k, d in edges:
                safe_add_edge(graph, u, node, k, d)

        for v, edges in succ_d.items():
            for k, d in edges:
                safe_add_edge(graph, node, v, k, d)


@uni_in_place_transformation
def enrich_grouping(universe, graph, function, relation):
    """Adds all of the grouped elements. See :func:`enrich_complexes`, :func:`enrich_composites`, and
    :func:`enrich_reactions`

    :param pybel.BELGraph universe: A BEL graph representing the universe of all knowledge
    :param pybel.BELGraph graph: The target BEL graph to enrich
    :param str function: The function by which the subject of each triple is filtered
    :param str relation: The relationship by which the predicate of each triple is filtered
    """
    nodes = list(get_nodes_by_function(graph, function))
    for u in nodes:
        for _, v, d in universe.out_edges_iter(u, data=True):
            if d[RELATION] != relation:
                continue

            if v not in graph:
                graph.add_node(v, attr_dict=universe.node[v])

            if v not in graph[u] or unqualified_edge_code[relation] not in graph[u][v]:
                graph.add_unqualified_edge(u, v, relation)


@uni_in_place_transformation
def enrich_complexes(universe, graph):
    """Add all of the members of the complex abundances to the graph.

    :param pybel.BELGraph universe: A BEL graph representing the universe of all knowledge
    :param pybel.BELGraph graph: The target BEL graph to enrich
    """
    enrich_grouping(universe, graph, COMPLEX, HAS_COMPONENT)


@uni_in_place_transformation
def enrich_composites(universe, graph):
    """Adds all of the members of the composite abundances to the graph.

    :param pybel.BELGraph universe: A BEL graph representing the universe of all knowledge
    :param pybel.BELGraph graph: The target BEL graph to enrich
    """
    enrich_grouping(universe, graph, COMPOSITE, HAS_COMPONENT)


@uni_in_place_transformation
def enrich_reactions(universe, graph):
    """Adds all of the reactants and products of reactions to the graph.

    :param pybel.BELGraph universe: A BEL graph representing the universe of all knowledge
    :param pybel.BELGraph graph: The target BEL graph to enrich
    """
    enrich_grouping(universe, graph, REACTION, HAS_REACTANT)
    enrich_grouping(universe, graph, REACTION, HAS_PRODUCT)


@uni_in_place_transformation
def enrich_variants(universe, graph, func=None):
    """Add the reference nodes for all variants of the given function.

    :param pybel.BELGraph universe: A BEL graph representing the universe of all knowledge
    :param pybel.BELGraph graph: The target BEL graph to enrich
    :param str or iter[str] func: The function by which the subject of each triple is filtered. Defaults to
                                      the set of protein, rna, mirna, and gene.
    """
    if func is None:
        func = {PROTEIN, RNA, MIRNA, GENE}

    nodes = list(get_nodes_by_function(graph, func))
    for u, v, d in universe.in_edges_iter(nodes, data=True):
        if d[RELATION] != HAS_VARIANT:
            continue

        if u not in graph:
            graph.add_node(u, attr_dict=universe.node[u])

        if v not in graph[u] or unqualified_edge_code[HAS_VARIANT] not in graph[u][v]:
            graph.add_unqualified_edge(u, v, HAS_VARIANT)


@uni_in_place_transformation
def enrich_unqualified(universe, graph):
    """Enrich the subgraph with the unqualified edges from the graph.

    :param pybel.BELGraph universe: A BEL graph representing the universe of all knowledge
    :param pybel.BELGraph graph: The target BEL graph to enrich

    The reason you might want to do this is you induce a subgraph from the original graph based on an annotation filter,
    but the unqualified edges that don't have annotations that most likely connect elements within your graph are
    not included.

    .. seealso::

        This function thinly wraps the successive application of the following functions:

        - :func:`enrich_complexes`
        - :func:`enrich_composites`
        - :func:`enrich_reactions`
        - :func:`enrich_variants`

    Equivalent to:

    >>> enrich_complexes(universe, graph)
    >>> enrich_composites(universe, graph)
    >>> enrich_reactions(universe, graph)
    >>> enrich_variants(universe, graph)
    """
    enrich_complexes(universe, graph)
    enrich_composites(universe, graph)
    enrich_reactions(universe, graph)
    enrich_variants(universe, graph)


# TODO should this bother checking multiple relationship types?
@uni_in_place_transformation
def expand_internal(universe, graph, edge_filters=None):
    """Edges between entities in the subgraph that pass the given filters

    :param pybel.BELGraph universe: The full graph
    :param pybel.BELGraph graph: A subgraph to find the upstream information
    :param edge_filters: Optional list of edge filter functions (graph, node, node, key, data) -> bool
    :type edge_filters: list or lambda
    """
    edge_filter = and_edge_predicates(edge_filters)

    for u, v in itt.product(graph, repeat=2):
        if graph.has_edge(u, v) or not universe.has_edge(u, v):
            continue

        rs = defaultdict(list)
        for k, d in universe[u][v].items():
            if not edge_filter(universe, u, v, k):
                continue

            rs[d[RELATION]].append(d)

        if 1 == len(rs):
            relation = list(rs)[0]
            for d in rs[relation]:
                graph.add_edge(u, v, attr_dict=d)
        else:
            log.debug('Multiple relationship types found between %s and %s', u, v)


@uni_in_place_transformation
def expand_internal_causal(universe, graph):
    """Adds causal edges between entities in the subgraph.

    Is an extremely thin wrapper around :func:`expand_internal`.

    :param pybel.BELGraph universe: A BEL graph representing the universe of all knowledge
    :param pybel.BELGraph graph: The target BEL graph to enrich with causal relations between contained nodes

    Equivalent to:

    >>> import pybel_tools as pbt
    >>> from pybel.struct.filters.edge_predicates import is_causal_relation
    >>> pbt.mutation.expand_internal(universe, graph, edge_filters=is_causal_relation)
    """
    expand_internal(universe, graph, edge_filters=is_causal_relation)
