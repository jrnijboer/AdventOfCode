from collections import defaultdict
def run(invalue, I, ip, offset):
    oc, outbuff = I[ip] % 100, []
    while oc != 99:
        m1, m2, m3 = I[ip] % 1000 // 100, I[ip] % 10000 // 1000, I[ip] // 10000
        val1 = I[I[ip + 1]] if m1 == 0 else I[ip + 1] if m1 == 1 else I[I[ip + 1] + offset]
        if oc not in [3,4,9]: val2 = I[I[ip + 2]] if m2 == 0 else I[ip + 2] if m2 == 1 else I[I[ip + 2] + offset]
        if oc in [1,2,7,8]: writeaddr = I[ip + 3] if m3 == 0 else I[ip + 3] + offset
        if oc == 3: writeaddr =I[ip + 1] if m1 == 0 else I[ip + 1] + offset
        if oc == 1: I[writeaddr] = val1 + val2
        elif oc == 2: I[writeaddr] = val1 * val2
        elif oc == 3: I[writeaddr] = invalue
        elif oc == 4 :
            if len(outbuff) == 0: outbuff = [val1]
            else:
                tmp = outbuff.pop()
                return [tmp, val1], ip + 2, offset
        elif oc == 5: ip = val2 - 2 if val1 != 0 else ip + 1
        elif oc == 6: ip = val2 - 2 if val1 == 0 else ip + 1
        elif oc == 7: I[writeaddr] = 1 if val1 < val2 else 0
        elif oc == 8: I[writeaddr] = 1 if val1 == val2 else 0
        elif oc == 9: offset += val1
        ip = ip + 4 if oc in [1,2,7,8] else ip + 2
        oc = I[ip] % 100
    return [], -1, 0

def solve(I, d, input):
    hull, pos, delta = defaultdict(int), (0,0), dict(zip('LRUD', [(-1, 0),(1, 0),(0, -1),(0, 1)]))
    ip, offset,hull[pos] = 0, 0, input
    while True:
        res, ip, offset = run(hull[pos], I, ip, offset)
        if ip < 0: break
        hull[pos] = res[0]
        d = 'URDL'[('URDL'.index(d) + (1 if res[1] == 1 else -1)) % 4]
        pos = (pos[0] + delta[d][0], pos[1] + delta[d][1])
    return hull

I = list(map(int,open("../input/day11.input").readline().split(",")))
D1 = D2 = {i:I[i] for i in range(len(I))}
print("answer a: {}\n".format(len(solve(defaultdict(int,D1), 'U', 0))))
hull = solve(defaultdict(int, D2), 'U', 1)
for y in range(7):
    for x in range(40):
        print("  " if hull[x,y]==0 else "##",end='')
    print()