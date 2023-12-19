from collections import defaultdict
from heapq import heappush, heappop

grid = open("../input/day17.txt", encoding="utf-8").read().strip().split("\n")
def traverse(minconsecutives, maxconsecutives):
    visited = set()
    Q = [(-1 * int(grid[0][0]), 0, 0, "", 0)]
    neighbours = {"^": (-1, 0), ">": (0, 1), "V": (1, 0), "<": (0, -1) }

    while Q:
        loss, row, col, prevdir, consecutives = heappop(Q)
        loss += int(grid[row][col])

        if row == len(grid)-1 and col == len(grid[0])-1 and consecutives >= minconsecutives:
            return loss
        if (row, col, prevdir, consecutives) in visited:
            continue

        visited.add((row, col, prevdir, consecutives))

        if consecutives < maxconsecutives and prevdir != "":
            dr, dc = neighbours[prevdir]
            if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid):
                heappush(Q, (loss, row + dr, col + dc, prevdir, consecutives + 1))

        if consecutives >= minconsecutives or loss == 0:
            for dir, (drn, dcn) in neighbours.items():
                if (dir == "V" and prevdir == "^") or (dir == "^" and prevdir == "V") \
                or (dir == "<" and prevdir == ">") or (dir == ">" and prevdir == "<") or dir == prevdir:
                    continue
                if 0 <= row + drn < len(grid) and 0 <= col + dcn < len(grid):
                    heappush(Q, (loss, row + drn, col + dcn, dir, 1))

print("Answer A:", traverse(1, 3))
print("Answer B:", traverse(4, 10))
