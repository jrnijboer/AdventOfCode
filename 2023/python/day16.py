from collections import defaultdict
grid = tuple(open("../input/day16.txt", encoding="utf-8").read().strip().split("\n"))

def energize(Q):
    seen = set()
    while Q:
        (row, col), (dr, dc) = Q.pop(0)
        if (row,col,dr,dc) in seen:
            continue
        seen.add((row,col,dr,dc))

        if (dr == 0 and grid[row][col] in "-.") or (dc == 0 and grid[row][col] in "|."):
            if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[row]):
                Q.append([(row + dr, col + dc ), (dr, dc)])
        elif (dr != 0 and grid[row][col] == "-"):
            if 0 <= row  < len(grid) and 0 <= col + 1 < len(grid[row]):
                Q.append([(row, col + 1 ), (0, 1)])
            if 0 <= row  < len(grid) and 0 <= col - 1 < len(grid[row]):
                Q.append([(row, col - 1 ), (0, -1)])
        elif (dc != 0 and grid[row][col] == "|"):
            if 0 <= row + 1 < len(grid) and 0 <= col < len(grid[row]):
                Q.append([(row + 1, col ), (1, 0)])
            if 0 <= row - 1 < len(grid) and 0 <= col < len(grid[row]):
                Q.append([(row - 1, col), (-1, 0)])
        elif grid[row][col] == "/":
            if 0 <= row - dc < len(grid) and 0 <= col - dr < len(grid[row]):
                Q.append([(row - dc, col - dr), (-dc, -dr)])
        elif grid[row][col] == "\\":
            if 0 <= row + dc < len(grid) and 0 <= col + dr < len(grid[row]):
                Q.append([(row + dc, col + dr), (dc, dr)])
    return len({(row, col) for row,col,_,_ in seen})

scoreB = 0
for i in range(len(grid)):
    scoreB = max(scoreB, energize([[(0, i), (1, 0)]]))
    scoreB = max(scoreB, energize([[(len(grid)-1, i),(-1, 0)]]))

for i in range(len(grid[0])):
    scoreB = max(scoreB, energize([[(i, 0), (0, 1)]]))
    scoreB = max(scoreB, energize([[(len(grid[0])-1, i),(0, -1)]]))

print("Answer A:", energize([[(0, 0), (0, 1)]]))
print("Answer B:", scoreB)
