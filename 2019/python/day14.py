from collections import defaultdict
input = [line for line in open("../input/day14.input").readlines()]
R, Rq = {}, {}
for r in input:
    i, o = r.strip().split(" => ")
    q, o = o.split(" ")
    Rq[o] = int(q)
    l, inItems = [], i.split(", ")
    for t in inItems:
        l.append((t.split(" ")[1], int(t.split(" ")[0])))
    R[o] = l

def BuildRequirements(output, q):
    for r in R[output]:
        if r[0] == "ORE": O[output] += q
        else:
            N = (r[1] * q + Rq[output] - 1) // Rq[output] #int(ceil(a/b))
            if stock[r[0]] > 0:
                if N > stock[r[0]]:
                    t = stock[r[0]]
                    stock[r[0]] -= t
                    N -= t
                else:
                    stock[r[0]] -= N
                    N = 0
            stock[r[0]] += ((N + Rq[r[0]] - 1) // Rq[r[0]]) * Rq[r[0]] - N
            BuildRequirements(r[0], (N + Rq[r[0]] - 1) // Rq[r[0]]* Rq[r[0]])

O, stock = defaultdict(int), defaultdict(int)
BuildRequirements("FUEL", 1)
print("answer a: {}".format(sum([O[r]//Rq[r] * R[r][0][1]  for r in O.keys()])))

low, high = 0, 1000000000000
while low < high:
    mid, O, stock = (low+high+1) // 2, defaultdict(int), defaultdict(int)
    BuildRequirements("FUEL", mid)
    if sum([O[r]//Rq[r] * R[r][0][1] for r in O.keys()]) <= 1000000000000: low = mid
    else: high = mid -1
print("answer b: {}".format(mid))