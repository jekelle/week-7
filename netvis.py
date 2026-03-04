import networkx as nx
from pyvis.network import Network



G = nx.read_graphml('./G.graphml')

vis = Network(width="100%", select_menu=False, filter_menu=False)
vis.from_nx(G)

vis.show_buttons(filter_=['nodes', 'physics'])
vis.show('net.html', notebook=False)
