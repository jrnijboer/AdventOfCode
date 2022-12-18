from itertools import combinations
from collections import deque, defaultdict
lines = [line.strip() for line in open("../input/day16.input", encoding="utf-8").readlines()]
distances, tunnels, valverates = {}, {}, {"AA": 0}

for line in lines:
    parts = line.split()
    source = parts[1]
    rate = int(parts[4].split("=")[1].replace(";",""))
    destinations = parts[9:]
    for i, d in enumerate(destinations):
        destinations[i] = d.replace(",", "")
    tunnels[source] = destinations
    if rate > 0:
        valverates[source] = rate

routes = combinations(valverates.keys(), 2)
for start, end in routes:
    best = 999
    Q = deque([(start, 0, set())])
    while Q:
        location, distance, visited = Q.popleft()
        if location == end:
            if distance < best:
                distances[(start, end)] = distance
                distances[(end, start)] = distance
                best = distance
            continue
        visited.add(location)
        for dest in tunnels[location]:
            if dest not in visited:
                Q.append((dest, distance + 1, visited))
destinations = set(valverates.keys()) - {"AA"}

maxpressure = 0
Q = deque([("AA", 0, 0, destinations)])
timelimit = 30
while Q:
    location, time, pressure, destinations = Q.popleft()
    pressure = pressure + (timelimit - time - 1) * valverates[location]
    maxpressure = max(maxpressure, pressure)
    for dest in destinations:
        time_needed = 1 + distances[(location, dest)]
        if location == "AA":
            time_needed -= 1
        if time + time_needed < timelimit:
            Q.append((dest, time + time_needed, pressure, destinations - {dest}))
print("Answer A:", maxpressure)

destinations = frozenset(valverates.keys()) - {"AA"}
Q = deque([("AA", 0, 0, frozenset())])
timelimit = 26
B = defaultdict(int)
while Q:
    location, time, pressure, seen = Q.popleft()
    pressure = pressure + (timelimit - time - 1) * valverates[location]
    B[seen] = max(B[seen], pressure)
    for dest in destinations - seen:
        time_needed = 1 + distances[(location, dest)]
        if location == "AA":
            time_needed -= 1
        if time + time_needed < timelimit:
            Q.append((dest, time + time_needed, pressure, seen | {dest}))
print("Answer B:", max(v1 + v2 for (k1, v1), (k2, v2) in combinations(B.items(), 2) if not k1 & k2))
