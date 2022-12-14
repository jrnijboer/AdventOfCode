def solve(offset, partB = False):
    lines = [line.strip() for line in open("../input/day14.input", encoding="utf-8").readlines()]
    c, maxY, minX, maxX, i = {}, 0, 1e9, 0, 0

    for points in [line.split(" -> ") for line in lines]:
        for ix in range(1, len(points)):
            x1, y1 = [int(n) for n in points[ix -1].split(",")]
            x2, y2 = [int(n) for n in points[ix].split(",")]
            maxY, minX, maxX = max(y1, y2, maxY), min(x1, x2, minX), max(x1, x2, maxX)
            for x in range(min(x1, x2), 1 + max(x1, x2)):
                for y in range(min(y1, y2), 1 + max(y1, y2)):
                    c[(x,y)]= "#"

    while True:
        sandX, sandY = 500, 0
        while sandY < maxY + offset:
            if (sandX, sandY + 1) not in c:
                sandY += 1
            elif (sandX -1, sandY + 1) not in c:
                sandX, sandY = sandX -1, sandY + 1
            elif (sandX + 1, sandY + 1) not in c:
                sandX, sandY = sandX + 1, sandY + 1
            else:
                c[(sandX,sandY)] = "O"
                break
        if sandY == maxY + offset and partB:
            c[(sandX, sandY)] = "O"
        elif sandY == 0 and partB or sandY >= maxY and not partB:
            return i + offset
        i += 1

print("Answer A:", solve(0, False))
print("Answer B:", solve(1, True))
