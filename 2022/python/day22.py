import re
from collections import defaultdict

D = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)} #RDLU

def solve(partA=True):
    gridlines, directions = open("../input/day22.input", encoding="utf-8").read().split("\n\n")
    G = defaultdict(str)
    maxx = 0
    gridlines = gridlines.split("\n")
    for y, line in enumerate(gridlines):
        maxx = max(len(line), maxx)
        for x, cell in enumerate(line):
            if cell in ".#":
                G[y,x] = cell

    direction = 0
    pos = (0, gridlines[0].index("."))
    for part in re.split('([RL])', directions):
        if part == "L":
            direction = (direction - 1) % 4
        elif part == "R":
            direction = (direction + 1) % 4
        else:
            dy, dx = D[direction]
            cur_dy, cur_dx, cur_direction = dy, dx, direction
            steps = int(part)
            while steps > 0:
                miny, minx = 999999, 999999
                maxy, maxx = 0, 0
                for (y, x) in G:
                    if x == pos[1]:
                        miny = min(y, miny)
                        maxy = max(y, maxy)
                    if y == pos[0]:
                        minx = min(x, minx)
                        maxx = max(x, maxx)
                newy, newx = pos

                if partA:
                    newy = (pos[0] + dy - miny) % (1 + maxy - miny) + miny
                    newx = (pos[1] + dx - minx) % (1 + maxx - minx) + minx
                elif not partA:
                    cur_dy, cur_dx = dy, dx
                    cur_direction = direction
                    if pos[0] == 0 and 50 <= pos[1] < 100 and direction == 3: #up, orange to yellow
                        newy = pos[1] + 100
                        newx = 0
                        dy, dx = D[0] # right
                        direction = 0
                    elif 150 <= pos[0] < 200 and pos[1] == 0 and direction == 2: #left, yellow to orange
                        newy = 0
                        newx = pos[0] - 100
                        dy, dx = D[1]  #down
                        direction = 1
                    elif pos[0] == 0 and 100 <= pos[1] < 150 and direction == 3: #up, blue to yellow
                        newy = 199
                        newx = pos[1] - 100
                    elif pos[0] == 199 and 0 <= pos[1] < 50 and direction == 1: #down, yellow to blue
                        newy = 0
                        newx = pos[1] + 100
                    elif 0 <= pos[0] < 50 and pos[1] == 149 and direction == 0: #right, blue to red
                        newy = 149 - pos[0]
                        newx = 99
                        dy, dx = D[2] #left
                        direction = 2
                    elif 100 <= pos[0] < 150 and pos[1] == 99 and direction == 0: #right, red to blue
                        newy = 149 - pos[0]
                        newx = 149
                        dy, dx = D[2] # left
                        direction = 2
                    elif pos[0] == 49 and 100 <= pos[1] < 150 and direction == 1: #down, blue to white
                        newy = pos[1] - 50
                        newx = 99
                        dy, dx = D[2] # left
                        direction = 2
                    elif 50 <= pos[0] < 100 and pos[1] == 99 and direction == 0: #right, white to blue
                        newy = 49
                        newx = pos[0] + 50
                        dy, dx = D[3] # up
                        direction = 3
                    elif pos[0] == 149 and 50 <= pos[1] < 100 and direction == 1: #down, red to yellow
                        newy = pos[1] + 100
                        newx = 49
                        dy, dx = D[2] # left
                        direction = 2
                    elif 150 <= pos[0] < 200 and pos[1] == 49 and direction == 0: #right, yellow to red
                        newy = 149
                        newx = pos[0] - 100
                        dy, dx = D[3] #up
                        direction = 3
                    elif pos[0] == 100 and 0 <= pos[1] < 50 and direction == 3: # up, green to white
                        newy = pos[1] + 50
                        newx = 50
                        dy, dx = D[0] #right
                        direction = 0
                    elif 50 <= pos[0] < 100 and pos[1] == 50 and direction == 2: #left, white to green
                        newy = 100
                        newx = pos[0] - 50
                        dy, dx = D[1] #down
                        direction = 1
                    elif 0 <= pos[0] < 50 and pos[1] == 50 and direction == 2: #left, orange to green
                        newy = 149 - pos[0]
                        newx = 0
                        dy, dx = D[0] #right
                        direction = 0
                    elif 100 <= pos[0] < 150 and pos[1] == 0 and direction == 2: #left, green to orange
                        newy = 149 - pos[0]
                        newx = 50
                        dy, dx = D[0] #right
                        direction = 0
                    else:
                        newy = (pos[0] + dy - miny) % (1 + maxy - miny) + miny
                        newx = (pos[1] + dx - minx) % (1 + maxx - minx) + minx
                if G[(newy, newx)] == "#":
                    dy, dx = cur_dy, cur_dx
                    direction = cur_direction
                    break
                steps -= 1
                pos = (newy, newx)

    return (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + direction

print("Answer A:", solve(partA = True))
print("Answer B:", solve(partA = False))
