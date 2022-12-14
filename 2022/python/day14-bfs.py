from collections import deque
lines = [line.strip() for line in open("../input/day14.input", encoding="utf-8").readlines()]
c, maxY, minX, maxX, i, Q = {}, 0, 500, 0, 0, deque([(500, 0)])

for points in [line.split(" -> ") for line in lines]:
    for ix in range(1, len(points)):
        x1, y1 = [int(n) for n in points[ix -1].split(",")]
        x2, y2 = [int(n) for n in points[ix].split(",")]
        maxY, minX, maxX = max(y1, y2, maxY), min(x1, x2, minX), max(x1, x2, maxX)
        for x in range(min(x1, x2), 1 + max(x1, x2)):
            for y in range(min(y1, y2), 1 + max(y1, y2)):
                c[(x,y)]= "#"
rockcount = len(c)

def printGrid(startX, width):
    for y in range(maxY + 3):
        for x in range(startX, startX + width):
            if (x,y) in c:
                print(c[(x,y)], end="")
            else:
                if y == maxY + 2:
                    print("#", end = "")
                else:
                    print(".", end="")
        print()
    print("\n********************\n")

while True:
    sandX, sandY = 500, 0
    while sandY < maxY:
        if (sandX, sandY + 1) not in c:
            sandY += 1
        elif (sandX -1, sandY + 1) not in c:
            sandX, sandY = sandX -1, sandY + 1
        elif (sandX + 1, sandY + 1) not in c:
            sandX, sandY = sandX + 1, sandY + 1
        else:
            c[(sandX,sandY)] = "O"
            break
    if sandY >= maxY:
        # printGrid(minX - 5, maxX - minX + 10)
        print("Answer A:", i)
        break
    i += 1

while Q:
    sandX, sandY = Q.popleft()
    if sandY == maxY + 1:
        continue
    if (sandX, sandY + 1) not in c:
        c[(sandX, sandY + 1)] = "O"
        Q.append((sandX, sandY + 1))
    if (sandX - 1, sandY + 1) not in c:
        c[(sandX - 1, sandY + 1)] = "O"
        Q.append((sandX -1, sandY + 1))
    if (sandX + 1, sandY + 1) not in c:
        c[(sandX + 1, sandY + 1)] = "O"
        Q.append((sandX +1, sandY + 1))
# printGrid(min([p[0] for p in c]) - 2, 5 + max([p[0] for p in c]) - min([p[0] for p in c]))
print("Answer B:", len(c) - rockcount + 1)

