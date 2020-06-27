import networkx as nx

with open("input_6-1.txt") as file:
    data = file.readlines()
graph = nx.Graph(x.strip().split(")") for x in data)
print(sum(nx.shortest_path_length(graph, x, "COM") for x in graph.nodes))
print(nx.shortest_path_length(graph, "YOU", "SAN") - 2)