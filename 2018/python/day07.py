def solveA(reqs, nodes):
    while len(reqs) > 0:
        next = 'z'
        for k in sorted(reqs.keys()):
            if k > next:
                break 
            if reqs[k].issubset(nodes):
                next = k 
        reqs[next]= reqs[next].difference(nodes)
        if len(reqs[next]) == 0:
            del reqs[next]
        nodes.append(next)
    print("day 7, answer a", "".join(nodes))

def solveB(reqs, nodes):
    WORK, MAX_QUEUE, time = 60, 5, -1
    Q = {}
    for n in nodes:
        Q[n] = WORK + 1 + ord(n) - ord('A')
    nodes, available = list(), list()
    while len(Q.keys()) > 0:
        time += 1
        if min(Q.values()) == 0:
            handled = next(k for k, v in Q.items() if v == 0)
            nodes.append(handled)
            del Q[handled]
            keys = list(reqs.keys())
            for k in keys:
                if reqs[k].issubset(nodes):
                    available.append(k)
                    del reqs[k]
        available.sort()
        
        while len(Q) < MAX_QUEUE and len(available) > 0:
            c = available.pop(0)
            Q[c] = WORK + 1 + ord(c) - ord('A')
        for k in Q:            
            Q[k] -= 1

    print("day7, part b:", time, "".join(nodes))

input = [tuple(parts for parts in line.split(" ")) for line in open("../input/day7.input").readlines()]
reqs = {}
startnodes = set()
for row in input:
    startnodes.add(row[1])
    startnodes.add(row[7])
    if row[7] in reqs:
        reqs[row[7]].add(row[1])
    else:
        reqs[row[7]] = set(row[1])

startnodes = startnodes - set(reqs.keys())
solveA(reqs.copy(), sorted(startnodes))
solveB(reqs, sorted(startnodes))
