import networkx as nx
input = open("../input/day20.input").read()[1:-1]
pos, directions, G = 0 + 0j, [0 + 1j, 1 + 0j, 0 - 1j, -1 + 0j], nx.Graph()
closed, opened, positions, visited = [], [], {pos}, set()

for s in input:
    if s in "NESW":
        next = [p + directions["NESW".index(s)] for p in positions]
        for i in range(len(positions)):
            G.add_edge(list(positions)[i], next[i])
        positions = next
        visited.update(next)
    elif s == "(":
        closed.append(set())
        opened.append(positions)
    elif s == "|":
        closed[-1].update(positions)
        positions = opened[-1]
    elif s == ")":
        closed[-1].update(positions)
        opened.pop()
        positions = closed.pop()
print("Warning: calculating for about 60s")
distances = [nx.shortest_path_length(G, 0 + 0j, v) for v in visited]
print("Answer A:", max(distances))
print("Answer B:", len([d for d in distances if d >= 1000]))
