import math
from collections import defaultdict
input = [s.strip() for s in open("../input/day10.input").readlines()]
width, height, asteroids, M, destroyed = len(input[0]), len(input), [], 0, 0

for y in range(height):
    line = input[y]
    for x in range(width):
        if line[x] == '#': asteroids.append((x,y))

def getAngleAndDistance(s, t):
    dist = abs(t[0] - s[0]) + abs(t[1] - s[1])
    if t[1] == s[1]:
        if t[0] > s[0]: return 90.0, dist
        else: return -90.0, dist
    angle = math.degrees(math.atan2(t[0] - s[0],s[1] - t[1]))
    return angle if angle >= 0 else angle % 180 + 180 , dist

for a in asteroids:
    dests = set(asteroids).difference([a])
    targets = defaultdict(list)
    for t in dests:
        angle, distance = getAngleAndDistance(a, t)
        targets[angle].append((t, distance))
    if len(targets.keys()) > M:
        M, TargetDict = len(targets.keys()), targets

for k in TargetDict.keys():
    TargetDict[k] = sorted(TargetDict[k], key=lambda t: t[1])

while destroyed < 200:
    targets = sorted(list(TargetDict.keys()))
    for t in targets:
        val = TargetDict[t].pop(0)
        destroyed += 1
        if destroyed == 200: break
print("answer a: {}".format(M))
print("answer b: {}".format(val[0][0] * 100 + val[0][1]))