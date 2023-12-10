from collections import deque
lines = [[c for c in line.strip()] for line in open("../input/day10.txt", encoding="utf-8").readlines()]

for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if c == "S":
            position, sr, sc = (row, col), row, col #save startrow and startcol, to replace type
Q = deque([(position)])
loop = set(((position,)))

while Q:
    row, col = Q.popleft()
    if row > 0 and lines[row - 1][col] in "|F7" and lines[row][col] in "S|LJ" and (row - 1, col) not in loop:
        Q.append((row - 1, col))
        loop.add((row - 1, col))
    elif row < len(lines) - 1 and lines[row + 1][col] in "|LJ" and lines[row][col] in "S|F7" and (row + 1, col) not in loop:
        Q.append((row + 1, col))
        loop.add((row + 1, col))
    elif col > 0 and lines[row][col - 1] in "-FL" and lines[row][col] in "S-J7" and (row, col - 1) not in loop:
        Q.append((row, col - 1))
        loop.add((row, col - 1))
    elif col < len(lines[row]) - 1 and lines[row][col + 1] in "-J7" and lines[row][col] in "S-FL" and (row, col + 1) not in loop:
        Q.append((row, col + 1))
        loop.add((row, col + 1))

print("Answer A", len(loop) // 2)

if lines[sr - 1][sc] in "|7F" and lines[sr + 1][sc] in "JL|":
    S = "|"
elif lines[sr][sc + 1] in "-7J" and lines[sr + 1][sc] in "JL|":
    S = "F"
elif lines[sr - 1][sc] in "|7F" and lines[sr][sc + 1] in "-7J":
    S = "L"
elif lines[sr][sc - 1] in "-LF" and lines[sr][sc + 1] in "-7J":
    S = "-"
elif lines[sr][sc - 1] in "-LF" and lines[sr + 1][sc] in "JL|":
    S = "7"
elif lines[sr - 1][sc] in "|7F" and lines[sr][sc - 1] in "-LF":
    S = "J"
lines[sr][sc] = S

for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if (row, col) not in loop:
            lines[row][col] = "."
    #     print(lines[row][col], end='') #print cleaned up grid
    # print()

enclosed = set()
for row, line in enumerate(lines):
    for col, c in enumerate(line):
        if (row,col) in loop:
            continue
        wallcrossings = 0
        for d in range(col - 1, -1, -1):
            if lines[row][d] == "|":
                wallcrossings += 1
            elif lines[row][d] in"7J":
                entry = lines[row][d]
            elif lines[row][d] in"FL":
                if entry == "7" and lines[row][d] == "L" or entry == "J" and lines[row][d] == "F":
                    wallcrossings += 1
        if wallcrossings % 2 != 0:
            enclosed.add((row,col))

print("Answer B:", len(enclosed))
