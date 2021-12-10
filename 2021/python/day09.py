from math import prod
lines = [i.strip() for i in open("../input/day09.input", encoding="utf-8").readlines()]
lows, G, C, R = [], {}, len(lines[0]), len(lines)
deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for row in range(R):
    for col in range(C):
        G[(col, row)] = int(lines[row][col])

for (col, row), height in G.items():
    if not ([G[(col + dc, row + dr)] for (dc, dr) in deltas
            if 0 <= dc + col < C and 0 <= dr + row < R and G[dc + col, dr + row] <= height]):
        lows.append((col, row))
print("Answer A:", sum(G[c, r] + 1 for c, r in lows))

B, productB = [], 1
for low in lows:
    Q, basin = [low], {low}
    while Q:
        pos = Q.pop()
        basin.add(pos)
        for d in deltas:
            c, r = pos[0] + d[0], pos[1] + d[1]
            if 0 <= c < C and 0 <= r < R and (c, r) not in basin and G[(c, r)] != 9:
                Q.append((pos[0] + d[0], pos[1] + d[1]))
    B.append(len(basin))
print("Answer B:", prod(list(sorted(B)[-3:])))
