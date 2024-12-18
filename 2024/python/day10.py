grid = [[int(c) for c in line.strip()] for line in open("../input/10.txt", encoding="utf-8").readlines()]
trailheads = [(x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == 0]
A, B = 0, 0

for x, y in trailheads:
    a, b = set(), 0
    Q = [(x, y, 0)]
    while Q:
        x, y, height = Q.pop(0)
        if height == 9:
            a.add((x, y))
            b += 1
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) and grid[y + dy][x + dx] == height + 1:
                Q.append((x+dx, y+dy, height+1))

    A += len(a)
    B += b

print("Answer A:", A)
print("Answer B:", B)
