import networkx
input = [line.strip() for line in open("../input/day25.input").readlines()]
points = [tuple(map(int, line.split(","))) for line in input]
g = networkx.Graph()
for x1, y1, z1, w1 in points:
    for x2, y2, z2, w2 in points:
        if abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) + abs(w1 - w2) <= 3:
            g.add_edge((x1, y1, z1, w1), (x2, y2, z2, w2))
print("Answer:", networkx.number_connected_components(g))
