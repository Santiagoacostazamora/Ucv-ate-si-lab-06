import matplotlib.pyplot as plt
import networkx as nx

from lab6_intelligent_search.graph.graph_builder import build_graph


def draw_graph():
    graph = build_graph()

    pos = nx.spring_layout(graph)

    nx.draw(
        graph,
        pos,
        with_labels=True,
        node_color='lightblue',
        node_size=2000,
        font_size=10
    )

    labels = nx.get_edge_attributes(graph, 'weight')

    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=labels
    )

    plt.title('Grafo de búsqueda')
    plt.show()
