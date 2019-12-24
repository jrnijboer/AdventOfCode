from collections import defaultdict
input = open("../input/day24.input").readlines()
G = defaultdict(int)
for y in range(5):
    for x in range(5): G[x,y] = input[y][x]

def printGrid(g):
    for y in range(5):
        for x in range(5): print(g[x,y], end='')           
        print()

def getState(grid):
    s = 0
    for y in range(5):
        for x in range(5):
            if grid[x,y] == "#": s += 2 **(y * 5 + x)
    return s

def nextGrid(grid):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    g = defaultdict(int)
    for y in range(5):
        for x in range(5):
            adjacent = 0
            for d in deltas:
                if grid[x + d[0], y + d[1]] == "#": adjacent += 1
            if grid[x,y] == "#" and adjacent != 1: g[x,y] = "."
            elif grid[x,y] == "." and 1 <= adjacent <= 2: g[x,y] = "#"
            else: g[x,y] = grid[x,y]
    return g

states = {getState(G)}
while True:
    G = nextGrid(G)
    s = getState(G)
    if s in states:
        print("answer a: ", s)
        break
    else: states.add(s)

for y in range(5):
    for x in range(5): G[x,y] = input[y][x]
printGrid(G)