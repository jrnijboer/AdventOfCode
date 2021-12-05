from collections import defaultdict
lines = [i.strip().split("->") for i in open("../input/day05.input", encoding="utf-8").readlines()]

def make_grid(positions: list, useDiagonals: bool):
    G = defaultdict(int)
    for start, end in positions:
        startX, startY = (int(i) for i in start.split(","))
        endX, endY = (int(i) for i in end.split(","))
        dx = 1 if startX < endX else -1 if endX < startX else 0
        dy = 1 if startY < endY else -1 if endY < startY else 0

        if (not useDiagonals and (dx == 0 or dy == 0)) or useDiagonals:
            if dx == 0:
                xs = [startX for _ in range(startY, endY + dy, dy)]
            else:
                xs = range(startX, endX + dx, dx)
            if dy == 0:
                ys = [startY for _ in range(startX, endX + dx, dx)]
            else:
                ys = range(startY, endY + dy, dy)
            for x, y in zip(xs, ys):
                G[(x, y)] += 1
    return G

print("Answer A:", len([v for v in make_grid(lines, False).values() if v >= 2]))
print("Answer B:", len([v for v in make_grid(lines, True).values() if v >= 2]))
