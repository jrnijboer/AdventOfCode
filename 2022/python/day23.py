from collections import defaultdict
lines = [line.strip() for line in open("../input/day23.input", encoding="utf-8").readlines()]
E, D = set(), {"N":(-1, 0), "S": (1, 0), "W":(0, -1), "E": (0, 1), "NE": (-1, 1), "SE": (1, 1), "SW": (1, -1), "NW": (-1, -1)}
NSWE = {0: "N", 1: "S", 2: "W", 3:"E"}
adjacents = {0: ["N", "NW", "NE"], 1: ["S", "SE", "SW"], 2: ["W", "NW", "SW"], 3: ["E", "SE", "NE"]}
iterations, direction = 0, 0
minx, miny, maxy, maxx = 1000, 1000, 0, 0
for y, line in enumerate(lines):
    for x, square in enumerate(line):
        if square == "#":
            E.add((y, x))

while True :
    Enext = set()
    Emove = set()
    for (y, x) in E:
        hasNeighbours = False
        for _, (dy, dx) in D.items():
            if (y + dy, x + dx) in E:
                Emove.add((y, x))
                hasNeighbours = True
                break
        if not hasNeighbours:
            Enext.add((y, x))

    Q, proposed_positions = [], defaultdict(int)
    for (y, x) in Emove:
        moved = False
        for looking in range(4):
            hasNeighbours = False
            for d in adjacents[(direction + looking) % 4]:
                dy, dx = D[d]
                if (y + dy, x + dx) in E:
                    hasNeighbours = True
                    break
            if not hasNeighbours:
                dy, dx = D[NSWE[(direction + looking) % 4]]
                proposed_positions[(y + dy, x + dx)] += 1
                Q.append(((y, x), (y + dy, x + dx)))
                moved = True
                break
        if not moved:
            Enext.add((y, x))
    for (y, x), (newy, newx) in Q:
        if proposed_positions[(newy, newx)] > 1:
            Enext.add((y, x))
        else:
            Enext.add((newy, newx))

    if iterations == 10:
        for (y, x) in E:
            minx, miny = min(minx, x), min(miny, y)
            maxx, maxy = max(maxx, x), max(maxy, y)
        print("Answer A:", abs(maxx + 1 - minx) * abs(maxy + 1 - miny)  - len(E))
    iterations += 1
    if E == Enext:
        break
    E = Enext
    direction += 1

print("Answer B:", iterations)
