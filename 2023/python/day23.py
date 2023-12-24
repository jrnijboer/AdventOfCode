grid = open("../input/day23.txt").read().strip().splitlines()

start = tuple([(0, col) for col, ch in enumerate(grid[0]) if ch == "."][0])
dest = tuple([(len(grid) - 1, col) for col, ch in enumerate(grid[len(grid) - 1]) if ch == "."][0])

S =[(start, 0, set(((start,))))]
D = {"v": (1, 0), "<": (0, -1), "^": (-1, 0), ">": (0, 1)}

a = 0
while S:
    (row, col), moves, visited = S.pop()
    if (row, col) == dest:
        a = max(a, moves)

    if grid[row][col] in "<>v^":
        dr, dc = D[grid[row][col]]
        if (row + dr , col + dc) in visited or row + dr < 0 or row + dr >= len(grid) or col + dc < 0 or col + dc >= len(grid[0]) or grid[row+dr][col+dc] == "#":
            continue
        vnext = set(visited)
        vnext.add((row + dr , col + dc))
        S.append(((row + dr , col + dc), moves + 1, vnext))
    else:
        for (dr, dc) in D.values():
            if (row + dr , col + dc) in visited or row + dr < 0 or row + dr >= len(grid) or col + dc < 0 or col + dc >= len(grid[0]) or grid[row+dr][col+dc] == "#":
                continue
            vnext = set(visited)
            vnext.add((row + dr , col + dc))
            S.append(((row + dr , col + dc), moves + 1, vnext))

print("Answer A:", a)

junctions_fromto = {start:[], dest:[]}

for row, r in enumerate(grid):
    for col, ch in enumerate(r):
        if ch == "." and len([1 for (dr,dc) in D.values() if 0<=row +dr < len(grid) and 0<= col+dc < len(grid[0]) and grid[row+dr][col+dc] in ".<>^v" ]) >= 3:
            junctions_fromto[(row, col)] = []

for junction in junctions_fromto:
    visited = set(((junction),))
    Q = [(junction, 0)]
    while Q:
        (row, col), moves = Q.pop(0)
        if (row,col) != junction and (row,col) in junctions_fromto:
            junctions_fromto[junction].append(((row, col), moves))
            continue
        for (dr, dc) in D.values():
            if (row + dr , col + dc) in visited or row + dr < 0 or row + dr >= len(grid) or col + dc < 0 or col + dc >= len(grid[0]) or grid[row+dr][col+dc] == "#" or (row + dr , col + dc) in visited:
                continue
            visited.add((row + dr , col + dc))
            Q.append(((row + dr , col + dc), moves + 1))

def walk(junction, visited):
    if junction == dest:
        return 0
    longest = 0
    visited.add(junction)
    for j, dist in junctions_fromto[junction]:
        if j not in visited:
            longest = max(longest, dist + walk(j, set(visited)))
    return longest

print("Answer B:", walk(start, set()))
