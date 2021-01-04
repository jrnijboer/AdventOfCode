from collections import defaultdict
import heapq
depth, target = 7863, (14, 760)
target_x, target_y = target[0], target[1]
E = defaultdict(int)

risk = 0
for y in range(target[1] * 2):
    for x in range(target[0] * 10):
        geoindex = 0
        if x == 0 and y == 0:
            geoindex = 0
            E[(0,0)] = depth
        elif x == target[0] and y == target[1]:
            geoindex = 0
        elif y == 0:
            geoindex = 16807 * x
        elif x == 0:
           geoindex = 48271 * y
        else:
            geoindex = E[(x - 1, y)] * E[(x, y - 1)]
        E[(x,y)] = (geoindex + depth) % 20183
        if E[(x,y)] % 3 == 1 and x <= target[0] and y <= target[1]:
            risk += 1
        elif E[(x,y)] % 3 == 2 and x <= target[0] and y <= target[1]:
            risk += 2
print("Answer A:", risk)

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
#tools = torch, climbing, none
VISITED, Q = set(), [(0,0,0,0)]#Q: duration, x, y, tool

while Q:
    duration, curX, curY, tool = heapq.heappop(Q)
    if curX == target_x and curY == target_y and (tool == 0 or tool == 1):
        print("Answer B:", duration)
        break
    if (curX, curY, tool) in VISITED:
        continue
    VISITED.add((curX, curY,tool))

    area = E[(curX, curY)] % 3
    for tNext in range(3):
        if (area == 0 and (tNext == 0 or tNext == 1)) or (area == 1 and (tNext == 1 or tNext == 2)) or (area == 2 and (tNext == 0 or tNext == 2 )):
            heapq.heappush(Q, (duration + 7, curX, curY, tNext))
    for d in directions:
        neighbourX = curX + d[0]
        neighbourY = curY + d[1]
        area = E[(neighbourX, neighbourY)] % 3
        if not (0 <= neighbourX < target_x * 10 and 0 <= neighbourY < target_y * 2):
            continue
        if (area == 0 and (tool == 0 or tool == 1)) or (area == 1 and (tool == 1 or tool == 2)) or (area == 2 and (tool == 0 or tool == 2)):
            if (neighbourX, neighbourY, tNext) not in VISITED:
                heapq.heappush(Q, (duration + 1, neighbourX, neighbourY, tool))
