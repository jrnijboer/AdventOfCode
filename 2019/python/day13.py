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

blocks, I = 0, list(map(int,open("../input/day13.input").readline().split(",")))
D1 = D2 = {i:I[i] for i in range(len(I))}
D2[0], inbuff, ip = 2, [], 0
while True :
    game, ip, _ = run(inbuff, D2, ip, 0)
    if ip < 0: break
    for i in range(0, len(game), 3):
        if game[i+2] == 4: ball = game[i]
        elif game[i+2] == 3: paddle = game[i]
        elif game[i+2] == 2: blocks+=1
    inbuff = [0] if ball == paddle else [-1] if ball < paddle else [1]
print("answer a: {}".format(blocks))
print("answer b: {}".format(game[-1]))