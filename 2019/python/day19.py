from collections import defaultdict
import itertools
def run(inbuffer, I, ip, offset):
    I = defaultdict(int, I)
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

I = list(map(int,open("../input/day19.input").readline().split(",")))
a, xcount, firstx, G = 1, 0, 0, defaultdict(int)
for y in range(5, 2**32):
    xcount = 0
    if y == 50: print("answer a: ", a)
    for x in range(firstx, 2**32):        
        D = {i:I[i] for i in range(len(I))}
        res = run([x,y], D, 0, 0)[0][0]
        if res == 1:             
            if xcount == 0: firstx = x
            xcount += 1
            G[(x,y)] = 1
            a+=1
        if res == 0 and xcount > 0: break
    if G[(firstx + 99, y-99)] == 1: 
        print("answer b: ", (firstx * 10000) + y-99)
        break