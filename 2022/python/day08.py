trees = [line.strip() for line in open("../input/day08.input", encoding="utf-8").readlines()]
A, B = 0, 0
for x in range(1, len(trees) - 1):
    for y in range(1, len(trees) - 1):
        visleft, visright, visup, visdown, l, r, u, d = 1, 1, 1, 1, 0, 0, 0, 0
        for x1 in range(x, 0, -1):
            l += 1
            if trees[y][x1 -1] >= trees[y][x]:
                visleft = False
                break
        for x1 in range(x + 1, len(trees)):
            r += 1
            if trees[y][x1] >= trees[y][x]:
                visright = False
                break
        for y1 in range(y, 0, -1):
            u += 1
            if trees[y1 -1][x] >= trees[y][x]:
                visup = False
                break
        for y1 in range(y + 1, len(trees)):
            d += 1
            if trees[y1][x] >= trees[y][x]:
                visdown = False
                break
        B = max(l * r * u * d, B)
        A = A + 1 if any([visleft, visright, visup, visdown]) else A
print("Answer A:", A + len(trees) * 4 - 4)
print("Answer B:", B)
