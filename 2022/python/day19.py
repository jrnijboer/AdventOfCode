lines = [line.strip() for line in open("../input/day19.input", encoding="utf-8").readlines()]
resources = ["ore", "clay", "obsidian", "geode"]
blueprints = []
limits = {0:0, 1:0, 2:0, 3:1000}
for lineid, line in enumerate(lines):
    costs = {}
    parts = line.split()
    ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = list(map(int, [parts[6], parts[12], parts[18], parts[21], parts[27], parts[30]]))
    costs[0] = (ore_ore, 0, 0, 0)
    costs[1] = (clay_ore, 0, 0, 0)
    costs[2] = (obsidian_ore, obsidian_clay, 0, 0)
    costs[3] = (geode_ore, 0, geode_obsidian, 0)
    blueprints.append(costs)

def solve(timelimit, prints):
    blueprintgeodes = {}
    for blueprintid, blueprint in enumerate(prints):
        print(f"starting blueprint {blueprintid}...")
        seen = set()
        prodlimits = {0:0, 1:0, 2:0}
        maxgeodes = -1

        for i in range(4):
            prodlimits[0] = max(prodlimits[0], blueprint[i][0])
            prodlimits[1] = max(prodlimits[1], blueprint[i][1])
            prodlimits[2] = max(prodlimits[2], blueprint[i][2])

        Q = [(0, 1, 0, 0, 0, 0, 1, 0, 0, 0), (1, 1, 0, 0, 0, 0, 1, 0, 0, 0)]
        while Q:
            item = Q.pop()
            if item in seen:
                continue
            seen.add(item)
            requestedrobot, time, ore, clay, obsidian, geode, prodore, prodclay, prodobsidian, prodgeode = item
            builtrobot = False

            # buy phase
            buildcosts = blueprint[requestedrobot]
            if ore >= buildcosts[0] and clay >= buildcosts[1] and obsidian >= buildcosts[2]:
                ore -= buildcosts[0]
                clay -= buildcosts[1]
                obsidian -= buildcosts[2]
                builtrobot = True

            # collect ores phase
            ore += prodore
            clay += prodclay
            obsidian += prodobsidian
            geode += prodgeode

            # receive robot phase
            prodore += 1 if requestedrobot == 0 and builtrobot else 0
            prodclay += 1 if requestedrobot == 1 and builtrobot else 0
            prodobsidian += 1 if requestedrobot == 2 and builtrobot else 0
            prodgeode += 1 if requestedrobot == 3 and builtrobot else 0

            if time == timelimit:
                if geode > maxgeodes:
                    maxgeodes = geode
                continue

            # queue new robots or requeue current
            if builtrobot:
                if prodore < prodlimits[0]:
                    Q.append((0, time + 1, ore, clay, obsidian, geode, prodore, prodclay, prodobsidian, prodgeode))
                if prodclay < prodlimits[1]:
                    Q.append((1, time + 1, ore, clay, obsidian, geode, prodore, prodclay, prodobsidian, prodgeode))
                if prodclay > 0 and prodobsidian < prodlimits[2]:
                    Q.append((2, time + 1, ore, clay, obsidian, geode, prodore, prodclay, prodobsidian, prodgeode))
                if prodobsidian > 0:
                    Q.append((3, time + 1, ore, clay, obsidian, geode, prodore, prodclay, prodobsidian, prodgeode))
            else:
                Q.append((requestedrobot, time + 1, ore, clay, obsidian, geode, prodore, prodclay, prodobsidian, prodgeode))

        blueprintgeodes[blueprintid] = maxgeodes
        print(f"finished blueprint {blueprintid}")
    return blueprintgeodes

res = solve(24, blueprints)
a = sum([(k + 1) * v for k, v in res.items()])

res = solve(32, blueprints[:3])
b = 1
for v in res.values():
    b *= v
print("Answer A:", a)
print("Answer B:", b)
