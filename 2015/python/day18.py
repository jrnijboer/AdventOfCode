from collections import defaultdict

def GameOfLife(rounds, stuckCorners):
    lights = [line.strip() for line in open("../2015/input/day18.input", encoding="utf-8").readlines()]
    neighbours = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    grid = defaultdict(str)
    X, Y = len(lights[0]), len(lights)
    for y in range(len(lights)):
        for x in range(len(lights[y])):
            grid[(y, x)] = lights[y][x]

    if stuckCorners:
        grid[0, 0] = grid[0, X -1] = grid[Y-1, 0] = grid[Y-1, X -1] = "#"

    for i in range(rounds):
        newG = defaultdict(lambda:'.')
        for y in range(Y):
            for x in range(X):
                neighbourcount = len([n for n in neighbours if grid[(y + n[0], x + n[1])] == "#"])
                newG[(y, x)] = "#" if (grid[(y, x)] == "#" and (neighbourcount == 2 or neighbourcount == 3)) \
                                   or (grid[(y, x)] == "." and neighbourcount == 3) else "."
        grid = newG
        if stuckCorners:
            grid[0, 0] = grid[0, X -1] = grid[Y-1, 0] = grid[Y-1, X -1] = "#"
    return grid

print("Answer A:", len([light for light in GameOfLife(100, False).values() if light == "#"]))
print("Answer B:", len([light for light in GameOfLife(100, True).values() if light == "#"]))
