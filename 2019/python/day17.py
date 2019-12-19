from collections import defaultdict
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

I = list(map(int,open("../input/day17.input").readline().split(",")))
D, G = {i:I[i] for i in range(len(I))}, defaultdict(int)

output, _, _ = run([], D, 0, 0)
x, y, X = 0, 0, 0

for i in range(len(output)):
    if output[i] == 10:
        y+=1
        X = max(x, X)
        x=0
    else:
        G[(x,y)] = chr(output[i])
        if chr(output[i]) in "<>v^" : bot = (x,y)
        x+=1
a, Y, X = 0, y - 2, X -1

for y in range(1, y - 1) :
    for x in range(1, X - 1):
        if G[(x,y)] == "#" and G[(x + 1,y)] == "#" and G[(x -1 ,y)] == "#" and G[(x,y + 1)] == "#" and G[(x,y - 1)] == "#":
            a += x * y
print("answer a: {}".format(a))

def getTurn(pos, direction):
    if pos[0] > 0 and G[(pos[0] - 1,pos[1])] == "#" and direction == 0: return 1
    elif pos[0] < X and G[(pos[0] + 1,pos[1])] == "#" and direction == 0: return -1
    elif pos[0] > 0 and G[(pos[0] - 1,pos[1])] == "#" and direction == 2: return -1
    elif pos[0] < X and G[(pos[0] + 1,pos[1])] == "#" and direction == 2: return 1
    elif pos[1] > 0 and G[(pos[0], pos[1] - 1)] == "#" and direction == 1: return -1
    elif pos[1] < Y and G[(pos[0], pos[1] + 1)] == "#" and direction == 1: return 1
    elif pos[1] > 0 and G[(pos[0], pos[1] - 1)] == "#" and direction == 3: return 1
    elif pos[1] < Y and G[(pos[0], pos[1] + 1)] == "#" and direction == 3: return -1
    else: return 0

d=0
delta = ((0,-1), (-1,0), (0,1), (1,0)) #ULDR
while True:
    turn = getTurn(bot,d)
    if turn == 0 : break
    d, moves = (d + turn) % 4, 0

    while G[(bot[0] + delta[d][0], bot[1] + delta[d][1])] == "#":
        moves += 1
        bot = (bot[0] + delta[d][0], bot[1] + delta[d][1])

I = list(map(int,open("../input/day17.input").readline().split(",")))
D, G = {i:I[i] for i in range(len(I))}, defaultdict(int)

D[0] = 2
M = ['A','B','A','B','C','C','B','A','B','C']
A = ['L','4','R','8','L','6','L','10']
B = ['L','6','R','8','R','10','L','6','L','6']
C = ['L','4','L','4','L','10']

def toInstructions(S):
    return [ord(c) for c in ','.join([s for s in S])]

inbuffer = toInstructions(M) + [10] + toInstructions(A) + [10] + toInstructions(B) + [10] + toInstructions(C) + [10,ord('n'),10]
print("answer b: ", max(run(inbuffer, D, 0, 0)[0]))