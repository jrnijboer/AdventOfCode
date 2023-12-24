from itertools import combinations
from z3 import *

hailstones = open("../input/day24.txt").read().strip().splitlines()

H = {}
for h in hailstones:
    p, v = h.split(" @ ")
    x, y, z = map(int, (p.split(",")))
    dx, dy, dz = map(int, (v.split(",")))
    H[(x, y, z)] = (dx, dy, dz)

a = 0
for h1, h2 in combinations(H.keys(), 2):
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    x1, y1, _ = h1
    dx1, dy1, _ = H[h1]
    x2, y2 = x1 + dx1, y1 + dy1

    x3, y3, _ = h2
    dx2, dy2, _ = H[h2]
    x4, y4 = x3 + dx2, y3 + dy2

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if denominator == 0:
        continue

    Px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
    Py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
    if 200000000000000 <= Px <= 400000000000000 and 200000000000000 <= Py <= 400000000000000:
        if (Px - x2) * dx1 >= 0 and (Px - x4) * dx2 >= 0 and (Py - y2) * dy1 >= 0 and (Py - y4) * dy2 >= 0:
            a += 1

print("Answer A:", a)

x, y, z, dx, dy, dz = Int('x'), Int('y'), Int('z'), Int('dx'), Int('dy'), Int('dz')
solver = Solver()
for i, ((xh, yh, zh), (hdx, hdy, hdz) ) in enumerate(H.items()):
    time = Int('T' + str(i))
    solver.add(x + time * dx == (xh - time * hdx))
    solver.add(y + time * dy == (yh - time * hdy))
    solver.add(z + time * dz == (zh - time * hdz))
    if i == 3:
        break
res = solver.check()
model = solver.model()
print("Answer B:", model.eval(x + y + z))
