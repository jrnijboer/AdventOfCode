import copy, networkx as nx
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
I = list(map(int,open("../input/day15.input").readline().split(",")))
D, G = {i:I[i] for i in range(len(I))}, defaultdict(int)
G[(0,0)], P, S = 1, [(0,0)], [[1,2,3,4]]
B = [(0, D)] #ip, intcodes
N, maze = {1:[1,3,4], 2:[2,3,4], 3:[1,2,3], 4:[1,2,4]}, nx.Graph()

while len(S) > 0:   
    bot, moves, pos = B.pop(0), S.pop(0), P.pop(0)   
    for move in moves:
        d, ip = copy.deepcopy(bot[1]), bot[0]
        moveResult = run([move], d, ip, 0)[0][0]
        if move == 1: nextpos = (pos[0], pos[1] + 1)
        elif move == 2: nextpos = (pos[0], pos[1] - 1)
        elif move == 3: nextpos = (pos[0] - 1, pos[1])
        elif move == 4: nextpos = (pos[0] + 1, pos[1])
        if moveResult != 0:
            if nextpos not in G.keys():
                P.append(nextpos)
                S.append(N[move])
                B.append((ip, d))
                maze.add_edge(pos, nextpos)
            if moveResult == 2: O = nextpos
        G[nextpos] = moveResult
print("answer a: {}".format(nx.shortest_path_length(maze, (0, 0), O)))
print("answer b: {}".format(max([nx.shortest_path_length(maze, O, p) for p in G.keys() if G[p] != 0])))