_, _, xx, yy = open("../input/day17.input", encoding="utf-8").read().strip().split(" ")
minX, maxX = [int(i) for i in xx[2:-1].split("..")]
minY, maxY = [int(i) for i in yy[2:].split("..")]
minVx, maxVy = 0, minY * - 1 - 1
print("Answer A:", maxVy * (maxVy + 1) // 2)

while minVx * (minVx + 1) // 2 < minX:
    minVx += 1

def isHit(x, y, minX, maxX, minY, maxY):
    posX = posY = 0
    while posX <= maxX and posY >= minY:
        posX, posY = posX + x, posY + y
        if minX <= posX <= maxX and minY <= posY <= maxY:
            return True
        x = max(x - 1, 0)
        y -= 1
    return False

B = [(x, y) for x in range(minVx, maxX + 1) for y in range(minY, maxVy + 1)
     if isHit(x, y, minX, maxX, minY, maxY)]
print("Answer B:", len(B))
