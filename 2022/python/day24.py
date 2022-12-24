from collections import deque
startgrid = [line[1:-1] for line in open("../input/day24.input", encoding="utf-8").read().splitlines()][1:-1]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
width, height = len(startgrid[0]), len(startgrid)
begin, end = (-1, 0), (height, width -1)

def pathfind(destinations, time):
    start, finish = destinations.popleft()
    posy, posx = start
    seen = set()
    Q = deque([(posy, posx, time)])
    while Q:
        posy, posx, time = Q.popleft()
        if 0 <= posy < height:
            if startgrid[(posy - time) % height][posx] == "v":
                continue
            if startgrid[(posy + time) % height][posx] == "^":
                continue
            if startgrid[posy][(posx - time) % width] == ">":
                continue
            if startgrid[posy][(posx + time) % width] == "<":
                continue
        for dy, dx in directions:
            if (posy + dy, posx + dx) == finish:
                if destinations:
                    time = pathfind(destinations, time)
                return time
            if 0 <= posy + dy < height and 0 <= posx + dx < width and (posy + dy, posx + dx, time + 1) not in seen:
                seen.add((posy + dy, posx + dx, time + 1))
                Q.append((posy + dy, posx + dx, time + 1))
        Q.append((posy, posx, time + 1))
print("Answer A:", pathfind(deque([(begin, end)]), 0) + 1)
print("Answer B:", pathfind(deque([(begin, end),(end, begin), (begin, end)]), 0) + 1)
