from collections import defaultdict, deque
import networkx as nx
I = open("../input/day20.input").readlines()
height, width = len(I), len(I[0].strip('\n'))

TP = defaultdict(list)

for x in range(width):
    if "A" <= I[0][x] <= "Z":
        TP[I[0][x] + I[1][x]].append((x,2))
    if "A" <= I[height -1][x] <= "Z":
        TP[I[height-2][x] + I[height-1][x] ].append((x,height-3))
for y in range(height):
    if "A" <= I[y][0] <= "Z":
        TP[I[y][0] + I[y][1]].append((2,y))
    if "A" <= I[y][width -1 ] <= "Z":
        TP[I[y][width-2] + I[y][width -1] ].append((width-3,y))

innersquare=deque()
for y in range(2, height-3):
    for x in range(2, width -3):
        if I[y][x] == " ": innersquare.append((x,y))
topleft = innersquare.popleft()
bottomright = innersquare.pop()

for x in range(topleft[0], bottomright[0]):
    if "A" <= I[topleft[1]][x] <= "Z":
        TP[I[topleft[1]][x] + I[1 + topleft[1]][x]].append((x, topleft[1]-1))
    if "A" <= I[bottomright[1]][x] <= "Z":
        TP[I[bottomright[1] -1][x] + I[bottomright[1]][x]].append((x, bottomright[1]+1))
for y in range(topleft[1], bottomright[1]):
    if "A" <= I[y][topleft[0]] <= "Z":
        TP[I[y][topleft[0]] + I[y][topleft[0] + 1]].append((topleft[0] - 1, y))
    if "A" <= I[y][bottomright[0]] <= "Z":
        TP[I[y][bottomright[0] - 1] + I[y][bottomright[0]]].append((bottomright[0] + 1, y))

maze = nx.Graph()
z, deltas = 0, [(0,1), (0,-1), (-1,0), (1,0)]
for y in range(height):
    for x in range(width):
        if I[y][x] == ".":
            for d in deltas:
                if I[y + d[1]][x + d[0]] == ".":
                    maze.add_edge((x,y, z), (x+d[0], y+d[1], z))

for k in TP.keys():
    if k != "AA" and k != "ZZ":
        maze.add_edge((TP[k][0][0], TP[k][0][1], z),(TP[k][1][0], TP[k][1][1], z))
    else:
        TP[k] = (TP[k][0][0], TP[k][0][1], z)
print ("answer a: ", nx.shortest_path_length(maze, TP["AA"], TP["ZZ"]))

for k in TP.keys():
    if k != "AA" and k != "ZZ":
        maze.remove_edge((TP[k][0][0], TP[k][0][1], 0),(TP[k][1][0], TP[k][1][1], 0))

for z in range(1, 50):
    for y in range(height):
        for x in range(width):
            if I[y][x] == ".":
                for d in deltas:
                    if I[y + d[1]][x + d[0]] == ".":
                        maze.add_edge((x,y,z), (x+d[0], y+d[1], z))
    for k in TP.keys():
        if k != "AA" and k != "ZZ":
            maze.add_edge((TP[k][0][0], TP[k][0][1], z),(TP[k][1][0], TP[k][1][1], z-1))

print ("answer b: ", nx.shortest_path_length(maze, TP["AA"], TP["ZZ"]))