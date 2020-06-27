import networkx as nx
import pylab as plt

with open("input_6-1.txt") as file:
    data = file.readlines()
graph = nx.Graph()
for x in data:
    a, b, w = x.strip().split(")")
    graph.add_edge(a, b, weight=w)
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph,pos, edge_labels=labels)
plt.savefig('labels.png')
