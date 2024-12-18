from collections import deque
drops = [(int(x), int(y)) for x, y in (s.split(",") for s in open("../input/18.txt", encoding="utf-8").read().strip().split("\n"))]
dimension, grid, path = 71, set(), set()
S, E = (0, 0), (dimension - 1, dimension - 1)

for nanosecond, (bx, by) in enumerate(drops):
    grid.add((bx, by))
    if nanosecond < 1023 or (len(path) > 0 and (bx, by) not in path):
        continue
    Q = deque([(*S, 0,[])])
    visited, path = set(), set()
    while Q:
        x, y, dist, path = Q.popleft()
        if (x, y) == E:
            if nanosecond == 1023:
                print("Answer A:", dist)
            break
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= x + dx < dimension and 0 <= y + dy < dimension and (x + dx, y + dy) not in grid:
                Q.append((x + dx, y + dy, dist + 1, path + [(x + dx, y + dy)]))
    if not Q:
        print(f"Answer B: {bx},{by}")
        break
