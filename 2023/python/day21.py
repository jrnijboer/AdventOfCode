# explainer part B: https://github.com/villuna/aoc23/wiki/A-Geometric-solution-to-advent-of-code-2023,-day-21
grid = open("../input/day21.txt", encoding="utf-8").read().strip().split("\n")
S = [(r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S"][0]

def walk(row, col, steps):
    Q = [(row, col, steps)]
    DIR = {"D": (1, 0), "L": (0, -1), "U": (-1, 0), "R": (0, 1)}
    result = set()
    visited = set()

    while Q:
        row, col, steps = Q.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))

        if steps % 2 == 0:
            result.add((row, col))

        if steps == 0:
            continue

        for dr, dc in DIR.values():
            if row + dr < 0 or row + dr >= len(grid) or col + dc < 0 or col + dc >= len(grid[0]) or grid[row+dr][col+dc] == "#":
                continue
            Q.append((row+dr, col+dc, steps-1))
    return len(result)

print("Answer A:", walk(S[0],S[1], 64))

griddimension = len(grid) #131
even = walk(S[0], S[1], griddimension * 2)
odd = walk(S[0], S[1], griddimension * 2 + 1)
totalwidth = 1 + (26501365 - griddimension//2) // griddimension # 202301
fullgridreach = (totalwidth - 1) // 2 - 1
oddgrids = (totalwidth -2)**2
evengrids = (totalwidth -1)**2
filledgridscore = oddgrids * odd + evengrids*even
topcorner = walk(griddimension -1, S[1], griddimension-1)
bottomcorner = walk(0, S[1], griddimension-1)
leftcorner = walk(S[0], griddimension-1, griddimension-1)
rightcorner = walk(S[0], 0, griddimension-1)
topright_evencuts = walk(griddimension-1, 0, griddimension // 2 - 1) * (totalwidth - 1)
bottomright_evencuts = walk(0, 0, griddimension // 2 - 1) * (totalwidth - 1)
bottomleft_evencuts = walk(0, griddimension-1, griddimension // 2 - 1) * (totalwidth - 1)
topleft_evencuts = walk(griddimension-1, griddimension-1, griddimension // 2 - 1) * (totalwidth - 1)
topright_oddcuts = walk(griddimension-1, 0, griddimension // 2 * 3) * (totalwidth - 2)
bottomright_oddcuts = walk(0, 0, griddimension // 2 * 3) * (totalwidth - 2)
bottomleft_oddcuts = walk(0, griddimension-1, griddimension // 2 * 3) * (totalwidth - 2)
topleft_oddcuts = walk(griddimension-1, griddimension-1, griddimension // 2 * 3) * (totalwidth - 2)

answer = filledgridscore + topright_evencuts + bottomright_evencuts + bottomleft_evencuts + topleft_evencuts \
      + topright_oddcuts + bottomright_oddcuts + bottomleft_oddcuts + topleft_oddcuts + topcorner + rightcorner + bottomcorner+ leftcorner

print("Answer B:", answer)
