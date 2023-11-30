from itertools import permutations
lines = [line.strip() for line in open("../input/day09.input", encoding="utf-8").readlines()]
R, P = {}, set()
for line in lines:
    distance = int(line.split("= ")[1])
    p1, p2 = line.split(" = ")[0].split(" to ")
    R[(p1,p2)] = R[(p2,p1)] = distance
    P.add(p1)
    P.add(p2)

perms = list(permutations(P))
A, B = 1e10, 0
for route in perms:
    dist = 0
    for i in range(len(route) - 1):
        dist += R[(route[i], route[i+1])]
    A = min(dist, A)
    B = max(dist, B)

print("Answer A:", A)
print("Answer B:", B)
