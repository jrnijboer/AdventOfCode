from collections import defaultdict
lines = open("../input/day22.txt", encoding="utf-8").read().strip().split("\n")

leans = defaultdict(set)
supports = defaultdict(set)

def expand_shape(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    points = set()
    for x in range(min(x1,x2), max(x1,x2) + 1):
        for y in range(min(y1,y2), max(y1,y2) + 1):
            for z in range(min(z1,z2), max(z1,z2) + 1):
                points.add((x,y,z))
    return points

S = {}
all_pieces = {}
def drop(id, segments, fallen):
    prev = segments
    next = set()
    for x, y, z in segments:
        if z <= 1 or (x, y, z - 1) in fallen:
            S[id] = prev
            for xx, yy, zz in prev:
                assert (xx, yy, zz) not in all_pieces.keys()
                all_pieces[(xx, yy, zz)] = id
                if (xx, yy, zz-1) in all_pieces and id != all_pieces[(xx, yy, zz-1)]:
                    supports[all_pieces[xx, yy, zz-1]].add(id)
                    leans[id].add(all_pieces[xx, yy, zz-1])

            return fallen | prev
        next.add((x, y, z - 1))
    return drop(id, next, fallen)

def canIntegrate(id, fallen, S):
    maxZ = max([z for _, _, z in S[id]])
    for k, v  in S.items():
        minZ = min([z for _, _, z in v])
        if maxZ + 1 == minZ:
            if all([(x, y, z -1 ) not in fallen ^ S[id] for x, y, z in v if z == minZ]):
                return False
    return True

fallen = set()
bricks = []

for id, line in enumerate(lines):
    parts = line.split("~")
    p1 = tuple(map(int,parts[0].split(",")))
    p2 = tuple(map(int,parts[1].split(",")))
    bricks.append((p1,p2))

bricks.sort(key = lambda b: b[0][2])

for id, (p1, p2) in enumerate(bricks):
    segments = expand_shape(p1, p2)
    fallen = drop(id, segments, fallen)


a = sum([1 for k, v in S.items() if canIntegrate(k, fallen, S) ])
print("Answer A:", a)

total = 0
for id, _ in enumerate(bricks):
    supported = supports[id]
    Q = [s for s in supported if len(leans[s]) == 1]
    falling = set(Q)
    falling.add(id)
    while Q:
        b = Q.pop(0)
        for supported in supports[b]:
            if supported in falling:
                continue
            if all([l in falling for l in leans[supported]]):
                falling.add(supported)
                Q.append(supported)
    total += len(falling) - 1
print("Answer B:", total)
