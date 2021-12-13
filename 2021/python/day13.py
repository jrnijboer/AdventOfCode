from collections import defaultdict

def drawGrid(G: defaultdict, maxX: int, maxY: int):
    G = defaultdict(lambda: " ", G)
    for y in range(maxY + 1):
        for x in range(maxX + 1):
            print(G[(x, y)], end='')
        print()

points, folds = open("../input/day13.input", encoding="utf-8").read().split("\n\n")
G = {(int(x), int(y)): "#" for x, y in [p.split(",") for p in points.split("\n")]}
folds, A = folds.split("\n"), 0
maxx = max(p[0] for p in G.keys())
maxy = max(p[1] for p in G.keys())

for fold in folds:
    _, _, f = fold.split(" ")
    axis, n = f.split("=")
    if axis == "y":
        maxy //= 2
        G = {(k[0], k[1]) if k[1] < int(n) else (k[0], k[1] - 2 * (k[1] - int(n))): "#"
             for k in G.keys() if k[1] != int(n)}
    else:
        maxx //= 2
        G = {(k[0], k[1]) if k[0] < int(n) else (k[0] - 2 * (k[0] - int(n)), k[1]): "#"
             for k in G.keys() if k[0] != int(n)}
    if A == 0:
        A = len(G.values())

print("Answer A:", A)
print("Answer B:")
drawGrid(G, maxx, maxy)
