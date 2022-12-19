from collections import defaultdict
blasts = open("../input/day17.input", encoding="utf-8").read().strip()
shapes = [
    [(0,2),(0,3),(0,4),(0,5)],
    [(2,3),(1,2),(1,3),(1,4),(0,3)],
    [(2,4),(1,4),(0,2),(0,3),(0,4)],
    [(0,2),(1,2),(2,2),(3,2)],
    [(0,2),(0,3),(1,2),(1,3)]
]

def dropShape(grid, shapeindex, blaststring, bix):
    def moveShape(shape, dx, dy):
        for _, pos in enumerate(shape):
            if (pos[0] + dy, pos[1] + dx) in grid or pos[1] + dx < 0 or pos[1] + dx >= 7 or pos[0] + dy < 0:
                return shape
        return [(pos[0] + dy, pos[1] + dx) for pos in shape]

    top = max(y + 1 for (y, _) in grid) if grid else 0
    shape = moveShape(shapes[shapeindex], 0, top + 3)
    while True:
        dx = -1 if blaststring[bix] == "<" else 1
        shape = moveShape(shape, dx, 0)
        bix = (bix + 1) % len(blaststring)
        nextshape = moveShape(shape, 0, -1)
        if shape == nextshape:
            for _, pos in enumerate(shape):
                grid[pos] = "#"
            break
        shape = nextshape
    return grid, bix

G, fingerprints = defaultdict(str), {}
blastindex, turn, topY, cycleheight, trillion = 0, 0, 0, 0, 1000000000000
while turn < trillion:
    G, blastindex = dropShape(G, turn % 5, blasts, blastindex)
    topY = max(y + 1 for (y, _) in G)
    fingerprint = (blastindex, turn % 5, frozenset([(topY - y, x) for (y, x) in G if topY - y <= 30 ]))
    if fingerprint in fingerprints:
        (prevTurn, prevTop) = fingerprints[fingerprint]
        dtop = topY - prevTop
        dturn = turn - prevTurn
        cyclesleft = (trillion - turn) // dturn
        cycleheight += cyclesleft * dtop
        turn += cyclesleft * dturn
    fingerprints[fingerprint] = (turn, topY)
    turn += 1
    if turn == 2022:
        print("Answer A:", topY)
    G = {k:v for k, v in G.items() if k[0] >= topY - 50}
print("Answer B:", topY + cycleheight)
