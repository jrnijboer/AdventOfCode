grid = [list(line) for line in open("../input/20.txt", encoding="utf-8").read().split("\n")]
visited, sx,sy = set(), 0, 0
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char == "S":
            sx, sy = x, y

fair_path = [(sx, sy)]
while grid[sy][sx] != "E":
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if grid[sy + dy][sx + dx] != "#" and (sx + dx, sy + dy) not in visited:
            visited.add((sx + dx, sy + dy))
            fair_path.append((sx + dx, sy + dy))
            sx, sy = sx + dx, sy + dy
            break

fair_places = set(fair_path)
fair_indexes = {v: k for k, v in enumerate(fair_path)}

def cheat(max_cheats, min_gain):
    res = 0
    for ix, (x, y) in enumerate(fair_path):
        for dx in range(max_cheats * -1, max_cheats + 1):
            for dy in range(max_cheats * -1 + abs(dx), max_cheats + 1 - abs(dx)):
                if (x + dx, y + dy) in fair_places:
                    jx = fair_indexes[(x + dx, y + dy)]
                    manhattan_dist = abs(dx) + abs(dy)
                    if jx - ix - manhattan_dist >= min_gain:
                        res += 1
    return res

print("Answer A:", cheat(2, 100))
print("Answer B:", cheat(20, 100))
