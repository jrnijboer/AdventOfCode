import heapq

def manhattan(start: tuple, end: tuple) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def A_star(G, start, end):
    Q, seen, open = [(0, 0, start)], {start}, set([(0, 0)])
    while Q:
        current = heapq.heappop(Q)
        g_risk, pos = current[1], current[2]  # current[0] is f: g_risk + heuristic, not needed here
        open.remove(pos)
        if pos == end:
            return g_risk
        seen.add(pos)

        N = [(pos[0] + x, pos[1] + y) for x, y in D if (pos[0] + x, pos[1] + y) in G]
        for n in N:
            if n in seen or n in open:
                continue
            heapq.heappush(Q, (manhattan(n, end) + g_risk + G[n], g_risk + G[n], n))
            open.add(n)

lines = [line.strip() for line in open("../input/day15.input", encoding="utf-8").readlines()]
G = {}
for Y in range(len(lines)):
    for X, line in enumerate(lines[Y]):
        G[(X, Y)] = int(line)
    Y += 1
Y -= 1
start, end = (0, 0), (X, Y)
D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
print("Answer A:", A_star(G, start, end))

for y in range(Y + 1):
    for x in range(X + 1):
        for i in range(5):
            for j in range(5):
                next = G[(x, y)] + i + j
                if next > 9:
                    next -= 9
                G[(i * (X + 1) + x, j * (Y + 1) + y)] = next

print("Answer B:", A_star(G, start, ((X + 1) * 5 - 1, (Y + 1) * 5 - 1)))
