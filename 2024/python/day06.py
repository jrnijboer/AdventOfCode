G = [list(line.strip()) for line in open("../input/06.txt", encoding="utf-8")]
start = next((x, y) for y, row in enumerate(G) for x, char in enumerate(row) if char == "^")
dirs, B = [(0, -1), (1, 0), (0, 1), (-1, 0)], 0

def do_walk(x, y, grid):
    d, visited, loopdetector = 0, set(), set()
    dx, dy = dirs[d]
    while 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid) :
        if grid[y + dy][x + dx] != "#":
            x, y = x + dx, y + dy
            visited.add((x, y))
            if (x, y, d) in loopdetector:
                return visited, 1
            loopdetector.add((x, y, d))
        else:
            d = (d + 1) % 4
            dx, dy = dirs[d]
    return visited, 0

A, _ = do_walk(*start, G)
for x_block, y_block in A - {start}:
    G[y_block][x_block], tmp = "#", G[y_block][x_block]
    B += do_walk(*start, G)[1]
    G[y_block][x_block] = tmp
print("Answer A:", len(A))
print("Answer B:", B)
