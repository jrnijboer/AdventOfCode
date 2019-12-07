import itertools
def solve(invalue, I, ip):
    oc = I[ip] % 100
    while oc != 99:
        m1, m2 = I[ip] % 1000 // 100, I[ip] % 10000 // 1000
        val1 = I[ip + 1] if m1 == 1 else I[I[ip + 1]]
        if oc != 3 and oc != 4: val2 = I[ip + 2] if m2 == 1 else I[I[ip + 2]]
        if oc == 1: I[I[ip + 3]] = val1 + val2
        elif oc == 2: I[I[ip + 3]] = val1 * val2
        elif oc == 3: I[I[ip + 1]] = invalue
        elif oc == 4 : return val1, ip + 2
        elif oc == 5: ip = val2 - 2 if val1 != 0 else ip + 1
        elif oc == 6: ip = val2 - 2 if val1 == 0 else ip + 1
        elif oc == 7: I[I[ip + 3]]  = 1 if val1 < val2 else 0
        elif oc == 8: I[I[ip + 3]] = 1 if val1 == val2 else 0
        ip = ip + 4 if oc in [1,2,7,8] else ip + 2
        oc = I[ip] % 100
    return _, -1

def getAmps(phases):
    for p in phases:
        I = list(map(int,open("../input/day7.input").readline().split(",")))
        I[I[1]] = int(p)
        yield [I,2]

M = 0
for phases in itertools.permutations(str(43210)):
    res = 0
    amps = list(getAmps(phases))
    for a in amps:
        res, _ = solve(res, a[0], 2)
    M = max(M, res)
print("answer a: {}" .format(M))

M = 0
for phases in itertools.permutations(str(98765)):
    res, prev, currentAmp = 0, 0, 0
    amps = list(getAmps(phases))
    while amps[currentAmp][1] >= 0:
        res, amps[currentAmp][1] = solve(prev, amps[currentAmp][0], amps[currentAmp][1])
        if amps[currentAmp][1] < 0: break
        currentAmp, prev = (currentAmp + 1) % 5, res
    M = max(M, prev)
print("answer b: {}" .format(M))