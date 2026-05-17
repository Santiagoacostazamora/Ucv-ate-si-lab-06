import networkx as nx

from lab6_intelligent_search.graph.graph_builder import build_graph
from lab6_intelligent_search.graph.heuristic import heuristics


def heuristic(node1, node2):
    return heuristics[node1]


def find_route(start: str, goal: str):
    graph = build_graph()

    path = nx.astar_path(
        graph,
        start,
        goal,
        heuristic=heuristic,
        weight='weight'
    )

    cost = nx.path_weight(graph, path, weight='weight')

    return {
        'path': path,
        'cost': cost
    }