lines = [line.strip() for line in open("../input/day18.input", encoding="utf-8").readlines()]
A, B, blocks, visited = 0, set(), set(), set()
d = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
minx, miny, minz, maxx, maxy, maxz = 9999, 9999, 9999, 0, 0, 0
for line in lines:
    x, y, z = list(map(int,line.split(",")))
    blocks.add((x, y, z))
    minx, maxx = min(x, minx), max(x, maxx)
    miny, maxy = min(y, miny), max(y, maxy)
    minz, maxz = min(z, minz), max(z, maxz)

for x, y, z in blocks:
    for dx, dy, dz in d:
        if (x + dx, y + dy, z + dz) not in blocks:
            A += 1

Q = [(minx -1, miny -1, minz -1)]
while Q:
    x, y, z = Q.pop()
    visited.add((x, y, z))
    for dx, dy, dz in d:
        if (x + dx, y + dy, z + dz) in blocks:
            B.add((x, y, z) + ( x + dx, y + dy, z + dz))
        elif (x + dx, y + dy, z + dz) not in visited \
        and minz -1 <=(x + dx) <= maxx + 1 \
        and miny -1 <=(y + dy) <= maxy + 1 \
        and minz -1 <=(z + dz) <= maxz + 1:
            Q.append((x + dx, y + dy, z + dz))

print("Answer A:", A)
print("Answer B:", len(B))
