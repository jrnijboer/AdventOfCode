from collections import defaultdict
lines = open("../input/23.txt", encoding="utf-8").read().strip().split("\n")
A, B, connections = set(), set(), defaultdict(list)

for line in lines:
    from_node, to_node = line.split("-")
    connections[from_node].append(to_node)
    connections[to_node].append(from_node)

for x in connections:
    for y in connections[x]:
        for z in connections[y]:
            if x != z and x in connections[z]:
                A.add(tuple(sorted([x, y, z])))
print("Answer A:", len([nodes for nodes in A if any(node.startswith("t") for node in nodes)]))

for node, destinations in connections.items():
    cliques = defaultdict(int)
    for dest in destinations:
        cliques[dest] += 1
        for dest2 in connections[dest]:
            if dest2 != node:
                cliques[dest2] += 1
    max_clique_size = max(cliques.values())
    if max_clique_size > len(B):
        B = {node} | {k for k, v in cliques.items() if v == max_clique_size}
print("Answer B:", ",".join(sorted(list(B))))
