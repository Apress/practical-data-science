import networkx as nx

DG = nx.DiGraph([
        ('Start','Retrieve1'),
        ('Start','Retrieve2'),
        ('Retrieve1','Assess1'),
        ('Retrieve2','Assess2'),
        ('Assess1','Process'),
        ('Assess2','Process'),
        ('Process','Transform'),
        ('Transform','Report1'),
        ('Transform','Report2')
        ])

print("Unsorted Nodes")
print(DG.nodes())
print("Is a DAG?",nx.is_directed_acyclic_graph(DG))
sOrder=nx.topological_sort(DG)
print("Sorted Nodes")
print(sOrder)

pos=nx.spring_layout(DG)
nx.draw_networkx_nodes(DG,pos=pos,node_size = 1000)
nx.draw_networkx_edges(DG,pos=pos)
nx.draw_networkx_labels(DG,pos=pos)