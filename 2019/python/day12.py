import itertools
import numpy as np #warning: windows numpy is buggy/has an lcm method that overflows on large ints, linux works fine
def readInput():
    input = [line.strip().split(",") for line in open("../input/day12.input").readlines()]
    M = [[int((m[0][m[0].find("=") + 1:])), int((m[1][m[1].find("=") + 1:])), int((m[2][m[2].find("=") + 1:-1]))] for m in input]
    V = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    return M,V

def doTick(M, V):
    for (i,j) in itertools.combinations([0,1,2,3],2):
        for k in range(3):
            if M[i][k] < M[j][k]: V[i][k], V[j][k] = V[i][k] + 1, V[j][k] - 1
            elif M[i][k] > M[j][k]: V[i][k], V[j][k] = V[i][k] - 1, V[j][k] + 1
    for i in range(len(M)):
        for j in range(3): M[i][j] += V[i][j]

def getCyclus(coord):
    M, V = readInput()
    X, cyclus, done = [M[0][coord], M[1][coord], M[2][coord], M[3][coord]], 0, False
    while not done:
        doTick(M, V)
        cyclus += 1
        done = True
        for i in range(len(X)):
            if X[i] != M[i][coord] or V[i][coord] != 0:
                done = False
                break
    return cyclus

M, V = readInput()
for _ in range(1000): doTick(M, V)
print("answer a: {}".format(sum([sum([abs(p) for p in M[i]]) * sum([abs(p) for p in V[i]]) for i in range(len(M))])))
print("answer b: {}".format(np.lcm.reduce([getCyclus(0),getCyclus(1),getCyclus(2)])))