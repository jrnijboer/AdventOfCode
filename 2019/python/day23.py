from collections import defaultdict
def run(inbuffer, I, ip, offset):
    oc, outbuff = I[ip] % 100, []
    while oc != 99:
        m1, m2, m3 = I[ip] % 1000 // 100, I[ip] % 10000 // 1000, I[ip] // 10000
        val1 = I[I[ip + 1]] if m1 == 0 else I[ip + 1] if m1 == 1 else I[I[ip + 1] + offset]
        if oc not in [3,4,9]: val2 = I[I[ip + 2]] if m2 == 0 else I[ip + 2] if m2 == 1 else I[I[ip + 2] + offset]
        if oc in [1,2,7,8]: writeaddr = I[ip + 3] if m3 == 0 else I[ip + 3] + offset
        if oc == 3: writeaddr = I[ip + 1] if m1 == 0 else I[ip + 1] + offset
        if oc == 1: I[writeaddr] = val1 + val2
        elif oc == 2: I[writeaddr] = val1 * val2
        elif oc == 3:
            if len(inbuffer) == 0: return outbuff, ip, offset
            else: I[writeaddr] = inbuffer.pop(0)
        elif oc == 4: outbuff.append(val1)
        elif oc == 5: ip = val2 - 2 if val1 != 0 else ip + 1
        elif oc == 6: ip = val2 - 2 if val1 == 0 else ip + 1
        elif oc == 7: I[writeaddr] = 1 if val1 < val2 else 0
        elif oc == 8: I[writeaddr] = 1 if val1 == val2 else 0
        elif oc == 9: offset += val1
        ip = ip + 4 if oc in [1,2,7,8] else ip + 2
        oc = I[ip] % 100
    return outbuff, -1, 0

I = list(map(int,open("../input/day23.input").readline().split(",")))
N, P, O, Qin = {}, {}, {}, {}
for n in range(50): N[n], P[n], O[n], Qin[n] = defaultdict(int, {i:I[i] for i in range(len(I))}), 0, 0, [n]

done, partA, natY, natX, lastnat = False, False, 0, 0, -1
while not done:
    idle = 0
    for node in range(50):
        if len(Qin[node]) == 0:
            Qin[node] = [-1]
            idle+=1
        while len(Qin[node]) > 0:
            output, P[node], O[node] = run([Qin[node].pop(0)], N[node], P[node], O[node])
            while len(output) > 0:
                dest,x,y = output.pop(0), output.pop(0), output.pop(0)
                if dest == 255:
                    if not partA:
                        print("answer a: ", y)
                        partA = True
                    natY, natX = y, x
                else: Qin[dest].extend([x,y])
    if idle == 50:
        if lastnat == natY:
            print("answer b: ", y)
            done = True
        else:
            lastnat = natY
            Qin[0] = [natX, natY]