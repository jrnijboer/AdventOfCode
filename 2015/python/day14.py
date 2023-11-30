reindeerlines = [line.strip().split() for line in open("../input/day14.input", encoding="utf-8").readlines()]
R  = {}
for line in reindeerlines:
    R[line[0]] = [int(line[3]), int(line[6]), int(line[13])]

maxdistance, time = 0, 2503
for speed, duration, rest in R.values():
    cycles = time // (duration + rest)
    remaining = time % (cycles + rest)
    distance = cycles * speed * duration + min(duration, remaining) * speed
    maxdistance = max(maxdistance, distance)
print("Answer A:", maxdistance)

points = {k: 0 for k in R}
best = 0
distances = {k: 0 for k in R}

for time in range(1, 2503):
    for r, values in R.items():
        speed, duration, rest = values
        cycles = time // (duration + rest)
        remaining = time % (cycles + rest)
        distance = speed * (duration * (time // (duration + rest)) + min(time % (duration + rest), duration))
        distances[r] = distance

    maxdist = max(distances.values())
    for k, v in distances.items():
        if v == maxdist:
            points[k] += 1

print(f"Answer B: {max(points.values())}")
