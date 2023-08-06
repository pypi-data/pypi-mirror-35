# -*- coding: utf-8 -*-

"""The Unbiased Candidate Mechanism Generation workflow addresses the inconsistency in the definitions of the
boundaries of pathways, mechanisms, subgraphs, etc. in networks and systems biology that are introduced during curation
due to a variety of reasons.

A simple approach for generating unbiased candidate mechanisms is to take the upstream controlles


This module provides functions for generating subgraphs based around a single node, most likely a biological process.

Subgraphs induced around biological processes should prove to be subgraphs of the NeuroMMSig/canonical mechanisms
and provide an even more rich mechanism inventory.


Examples
~~~~~~~~
This method has been applied in the following Jupyter Notebooks:

- `Generating Unbiased Candidate Mechanisms <http://nbviewer.jupyter.org/github/pybel/pybel-notebooks/blob/master/algorithms/Generating%20Candidate%20Mechanisms.ipynb>`_
"""

from pybel.constants import BIOPROCESS
from pybel.struct import data_missing_key_builder, get_nodes_by_function
from pybel.struct.filters import filter_nodes
from pybel.struct.mutation import expand_upstream_causal, get_upstream_causal_subgraph
from pybel.struct.pipeline import in_place_transformation, transformation
from .constants import WEIGHT
from .mutation import collapse_consistent_edges, remove_inconsistent_edges

__all__ = [
    'remove_unweighted_leaves',
    'is_unweighted_source',
    'get_unweighted_sources',
    'remove_unweighted_sources',
    'prune_mechanism_by_data',
    'generate_mechanism',
    'generate_bioprocess_mechanisms',
]


def node_is_upstream_leaf(graph, node):
    """Return if the node is an upstream leaf. An upstream leaf is defined as a node that has no in-edges, and exactly
    1 out-edge.

    :param pybel.BELGraph graph: A BEL graph
    :param tuple node: A BEL node
    :return: If the node is an upstream leaf
    :rtype: bool
    """
    return 0 == len(graph.predecessors(node)) and 1 == len(graph.successors(node))


def get_upstream_leaves(graph):
    """Get all leaves of the graph (with no incoming edges and only one outgoing edge).

    .. seealso:: :func:`upstream_leaf_predicate`

    :param pybel.BELGraph graph: A BEL graph
    :return: An iterator over nodes that are upstream leaves
    :rtype: iter[tuple]
    """
    return filter_nodes(graph, node_is_upstream_leaf)


def get_unweighted_upstream_leaves(graph, key=None):
    """Get all leaves of the graph with no incoming edges, one outgoing edge, and without the given key in
    its data dictionary.

    .. seealso :: :func:`data_does_not_contain_key_builder`

    :param pybel.BELGraph graph: A BEL graph
    :param Optional[str] key: The key in the node data dictionary representing the experimental data. Defaults to
     :data:`pybel_tools.constants.WEIGHT`.
    :return: An iterable over leaves (nodes with an in-degree of 0) that don't have the given annotation
    :rtype: iter[tuple]
    """
    if key is None:
        key = WEIGHT

    return filter_nodes(graph, [node_is_upstream_leaf, data_missing_key_builder(key)])


@in_place_transformation
def remove_unweighted_leaves(graph, key=None):
    """Remove nodes that are leaves and that don't have a weight (or other key) attribute set.

    :param pybel.BELGraph graph: A BEL graph
    :param Optional[str] key: The key in the node data dictionary representing the experimental data. Defaults to
     :data:`pybel_tools.constants.WEIGHT`.
    """
    unweighted_leaves = list(get_unweighted_upstream_leaves(graph, key=key))
    graph.remove_nodes_from(unweighted_leaves)


def is_unweighted_source(graph, node, key):
    """Check if the node is both a source and also has an annotation.
    
    :param pybel.BELGraph graph: A BEL graph
    :param tuple node: A BEL node
    :param str key: The key in the node data dictionary representing the experimental data
    """
    return graph.in_degree(node) == 0 and key not in graph.node[node]


def get_unweighted_sources(graph, key=None):
    """Get nodes on the periphery of the subgraph that do not have a annotation for the given key.

    :param pybel.BELGraph graph: A BEL graph
    :param str key: The key in the node data dictionary representing the experimental data
    :return: An iterator over BEL nodes that are unannotated and on the periphery of this subgraph
    :rtype: iter[tuple]
    """
    if key is None:
        key = WEIGHT

    for node in graph:
        if is_unweighted_source(graph, node, key):
            yield node


@in_place_transformation
def remove_unweighted_sources(graph, key=None):
    """Prunes unannotated nodes on the periphery of the subgraph

    :param pybel.BELGraph graph: A BEL graph
    :param Optional[str] key: The key in the node data dictionary representing the experimental data. Defaults to
     :data:`pybel_tools.constants.WEIGHT`.
    """
    nodes = list(get_unweighted_sources(graph, key=key))
    graph.remove_nodes_from(nodes)


@in_place_transformation
def prune_mechanism_by_data(graph, key=None):
    """Removes all leaves and source nodes that don't have weights. Is a thin wrapper around 
    :func:`remove_unweighted_leaves` and :func:`remove_unweighted_sources`

    :param pybel.BELGraph graph: A BEL graph
    :param Optional[str] key: The key in the node data dictionary representing the experimental data. Defaults to
     :data:`pybel_tools.constants.WEIGHT`.

    Equivalent to:
    
    >>> remove_unweighted_leaves(graph)
    >>> remove_unweighted_sources(graph)
    """
    remove_unweighted_leaves(graph, key=key)
    remove_unweighted_sources(graph, key=key)


@transformation
def generate_mechanism(graph, node, key=None):
    """Generates a mechanistic subgraph upstream of the given node

    :param pybel.BELGraph graph: A BEL Graph
    :param tuple node: The target BEL node for generation
    :param Optional[str] key: The key in the node data dictionary representing the experimental data. Defaults to
     :data:`pybel_tools.constants.WEIGHT`.
    :return: A subgraph grown around the target BEL node
    :rtype: pybel.BELGraph
    """
    subgraph = get_upstream_causal_subgraph(graph, node)
    expand_upstream_causal(graph, subgraph)
    remove_inconsistent_edges(subgraph)
    collapse_consistent_edges(subgraph)

    if key is not None:  # FIXME when is it not pruned?
        prune_mechanism_by_data(subgraph, key)

    return subgraph


def generate_bioprocess_mechanisms(graph, key=None):
    """Generate a mechanistic subgraph for each biological process in the graph using :func:`generate_mechanism`

    :param pybel.BELGraph graph: A BEL Graph
    :param Optional[str] key: The key in the node data dictionary representing the experimental data. Defaults to
     :data:`pybel_tools.constants.WEIGHT`
    :return: A dictionary from {tuple bioprocess node: BELGraph candidate mechanism}
    :rtype: dict[tuple, pybel.BELGraph]
    """
    return {
        bp: generate_mechanism(graph, bp, key=key)
        for bp in get_nodes_by_function(graph, BIOPROCESS)
    }
