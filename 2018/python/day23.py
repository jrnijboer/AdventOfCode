#explanation: https://www.reddit.com/r/adventofcode/comments/a99n7x/2018_day_23_part_2_explanation_with_visualization/
#ported to python from https://github.com/Bodewes/AoC.2018/blob/54136d890649a138b2601b9964ba82bc1219f121/Day23/Program.cs
import re

def countBotsInCube(cube, bots):
    x, y, z, size = cube
    inRange = 0
    for botX, botY, botZ, botRange in bots:
        dist = 0
        if botX > x + size - 1:
            dist += abs(botX - (x + size - 1))
        elif botX < x:
            dist += abs(x - botX)
        if botY > y + size - 1:
            dist += abs(botY - (y + size - 1))
        elif botY < y:
            dist += abs(y - botY)
        if botZ > z + size - 1:
            dist += abs(botZ - (z + size - 1))
        elif botZ < z:
            dist += abs(z - botZ)

        if dist <= botRange:
            inRange += 1
    return inRange

input = open("../input/day23.input").read().split("\n")
B = []
pattern = r"pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)"
minX, minY, minZ = 999999999, 999999999, 999999999
maxX, maxY, maxZ = 0, 0, 0
for line in input:
    g = re.match(pattern, line)
    if (g):
        x, y, z, r = int(g.group(1)), int(g.group(2)), int(g.group(3)), int(g.group(4))
        minX, minY, minZ = min(minX, x), min(minY, y), min(minZ, z)
        maxX, maxY, maxZ = max(maxX, x), max(maxY, y), max(maxZ, z)
        B.append((x, y, z, r))
maxDim = max(maxX-minX, maxY-minY, maxZ-minZ)
startsize = 1
while startsize < maxDim:
    startsize *= 2
cubes = [(minX, minY, minZ, startsize, len(B))]

while cubes:
    # // sort, cube with most bots first, then by (manhattan) distance, then by size;
    cubes.sort(key = lambda x : (x[4] * -1, abs(x[0]) + abs(x[1]) + abs(x[2]), x[3]))
    x, y, z, size, botcount = cubes.pop(0)
    if size == 1:
        print("Answer B:", abs(x) + abs(y) + abs(z))
        break
    halfsize = size // 2
    #split cube in 8 smaller cubes
    s1 = (x,            y,            z,            halfsize)
    s2 = (x + halfsize, y,            z,            halfsize)
    s3 = (x,            y + halfsize, z,            halfsize)
    s4 = (x,            y,            z + halfsize, halfsize)
    s5 = (x + halfsize, y + halfsize, z,            halfsize)
    s6 = (x,            y + halfsize, z + halfsize, halfsize)
    s7 = (x + halfsize, y,            z + halfsize, halfsize)
    s8 = (x + halfsize, y + halfsize, z + halfsize, halfsize)

    nextcubes = [s1, s2, s3, s4, s5, s6, s7, s8]
    for c in nextcubes:
        c += (countBotsInCube(c, B),)
        if c[4] > 0:
            cubes.append(c)
