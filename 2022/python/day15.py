lines = [line.strip() for line in open("../input/day15.input", encoding="utf-8").readlines()]
targetY, rangeB = 2000000, 4000000
intervals, sensors, beaconsinrow = [], {}, set()
hi, lo = -999999999, 999999999
for line in lines:
    parts = line.split()
    x1, y1 = int(parts[2][2:-1]), int(parts[3][2:-1])
    x2, y2 = int(parts[8][2:-1]), int(parts[9][2:])

    sensorrange = abs(x1 - x2) + abs(y1 - y2)
    ydistance = abs(y1 - targetY)
    offset = sensorrange - ydistance
    sensors[(x1, y1)] = sensorrange

    if offset >= 0:
        lo, hi = min(x1 - offset, lo), max(x1 + offset, hi)
    if y2 == targetY:
        beaconsinrow.add(x2)
print("Answer A:", (hi - lo - len(beaconsinrow)) + 1 if lo < 0 else 0)

# copied from https://www.reddit.com/r/adventofcode/comments/zmcn64/comment/j0b90nr/?utm_source=reddit&utm_medium=web2x&context=3
aLineCoefs, bLineCoefs = set(), set()

for (x, y), srange in sensors.items(): # get all line coeffecients from the diamond shapes around the sensors
    aLineCoefs.add(y - x + srange + 1)
    aLineCoefs.add(y - x - srange - 1)
    bLineCoefs.add(x + y + srange + 1)
    bLineCoefs.add(x + y - srange - 1)
for a in aLineCoefs:
    for b in bLineCoefs:
        x, y = (b - a) // 2, (a + b) // 2 #intersection of line a and line b, this is where lines from 2 diamonds intersect
        if 0 <= x <= rangeB and 0 <= y <= rangeB:
            candidate = True
            for s, r in sensors.items(): # check if intersection point is in range of any sensor
                if abs(s[0] - x ) + abs(s[1] - y) <= r:
                    candidate = False
                    break
            if candidate:
                print("Answer B:", x * rangeB + y)
