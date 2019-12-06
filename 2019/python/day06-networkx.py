import networkx as nx
G, input = nx.Graph(), {k:v for (v,k) in [line.strip("\n").split(")") for line in open("../input/day6.input").readlines()]}
G.add_edges_from(input.items())
print("answer a: {}".format(sum([nx.shortest_path_length(G, k, "COM") for k, v in input.items()])))
print("answer b: {}".format(nx.shortest_path_length(G, "YOU", "SAN") - 2))