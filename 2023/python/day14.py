grid = tuple(open("../input/day14.txt", encoding="utf-8").read().splitlines())

def tilt(grid):
    G = [[c for c in line] for line in grid]
    for row, r in enumerate(G):
        for col, ch in enumerate(r):
            if ch == "O":
                res = 0
                for dr in range(row -1, -1, -1):
                    if G[dr][col] == ".":
                        res += 1
                    else:
                        break
                if res > 0:
                    G[row - res][col] = "O"
                    G[row][col] = "."
    G = tuple("".join(row) for row in G)
    return G

print("Answer A:", sum([s.count("O") * (len(grid) - row) for row, s in enumerate(tilt(grid))]))

grid = tuple(open("../input/day14.txt", encoding="utf-8").read().splitlines())
seen, turns, turn = set(grid), [grid], 0
while True:
    turn += 1
    for _ in range(4):
        grid = tilt(grid)
        grid = list(zip(*grid))
        grid = [grid[i][::-1] for i,_ in enumerate(grid)]

    if tuple(["".join(x) for x in grid]) in seen:
        break
    seen.add(tuple(["".join(x) for x in grid]))
    turns.append(tuple(["".join(x) for x in grid]))

first = turns.index(tuple(["".join(x) for x in grid]))
grid = turns[(1000000000 - first) % (turn - first) + first]
print("Answer B:", sum([s.count("O") * (len(grid) - row) for row, s in enumerate(grid)]))
