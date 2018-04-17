# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt
G=nx.DiGraph()
G.add_weighted_edges_from([('s', 'u' ,100), ('s' ,'x' ,50),
                               ('u', 'v' ,10), ('u' ,'x' ,20),
                               ('v', 'y' ,10), ('x' ,'u' ,30),
                               ('x', 'v' ,50), ('x' ,'y' ,20),
                               ('y', 's' ,70), ('y' ,'v' ,60)])
G.add_node('s', demand = -1)
G.add_node('v', demand = 1)
flowCost, flowDict = nx.network_simplex(G)
print(sorted([(u, v) for u in flowDict for v in flowDict[u] if flowDict[u][v] > 0]))
print(nx.info(G, n=None))
print('Travel from S to V')
print(nx.shortest_path(G, 's', 'v', weight = 'weight'))
print(nx.shortest_path_length(G, 's', 'v', weight = 'weight'),'miles')
print('Travel from V to S')
print(nx.shortest_path(G, 'v', 's', weight = 'weight'))
print(nx.shortest_path_length(G, 'v', 's', weight = 'weight'),'miles')

plt.figure(figsize=(10, 10))
pos=nx.circular_layout(G)
nx.draw_networkx_edge_labels(G,pos=pos)
nx.draw_networkx(G, pos=pos, arrows=True, with_labels=True,\
                 node_size=1000,font_size=20,node_shape='D')
limits=plt.axis('off')
plt.show()

G.add_weighted_edges_from([('s', 'a' ,2), ('a' ,'x' ,5)])


flowCost, flowDict = nx.network_simplex(G)
print(sorted([(u, v) for u in flowDict for v in flowDict[u] if flowDict[u][v] > 0]))
print(nx.info(G, n=None))
print('Travel from S to V')
print(nx.shortest_path(G, 's', 'v', weight = 'weight'))
print(nx.shortest_path_length(G, 's', 'v', weight = 'weight'),'miles')
print('Travel from V to S')
print(nx.shortest_path(G, 'v', 's', weight = 'weight'))
print(nx.shortest_path_length(G, 'v', 's', weight = 'weight'),'miles')

plt.figure(figsize=(10, 10))
pos=nx.circular_layout(G)
nx.draw_networkx_edge_labels(G,pos=pos)
nx.draw_networkx(G, pos=pos, arrows=True, with_labels=True,\
                 node_size=1000,font_size=20,node_shape='D')
limits=plt.axis('off')
plt.show()