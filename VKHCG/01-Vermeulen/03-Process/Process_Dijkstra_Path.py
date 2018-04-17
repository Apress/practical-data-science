# -*- coding: utf-8 -*-


import networkx as nx
G = nx.Graph()
G.add_edge('a', 'c', weight=1)
G.add_edge('a', 'd', weight=2)
G.add_edge('b', 'c', weight=2)
G.add_edge('c', 'd', weight=1)
G.add_edge('b', 'f', weight=3)
G.add_edge('c', 'e', weight=3)
G.add_edge('e', 'f', weight=2)
G.add_edge('d', 'g', weight=1)
G.add_edge('g', 'f', weight=1)

d=nx.dijkstra_path(G, source='a', target='f', weight=None)

print(d)