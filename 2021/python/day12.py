from collections import defaultdict

N = defaultdict(list)
for line in [i.strip() for i in open("../input/day12.input", encoding="utf-8").readlines()]:
    k, v = line.split("-")
    N[k].append(v)
    N[v].append(k)

def solve(allowTwice: bool):
    routeCount, Q = 0, [("start", set(), False)]
    while Q:
        pos, smallSeen, twice = Q.pop()
        if pos == "end":
            routeCount += 1
        else:
            for n in N[pos]:
                if n not in smallSeen and n != "start":
                    sNext = set(smallSeen)
                    if n.islower():
                        sNext.add(n)
                    Q.append((n, sNext, twice))
                elif n in smallSeen and not twice and allowTwice and n not in ["start", "end"]:
                    Q.append((n, smallSeen, True))
    return routeCount

print("Answer A:", solve(False))
print("Answer B:", solve(True))
