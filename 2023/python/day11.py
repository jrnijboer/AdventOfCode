from itertools import combinations
lines = [line.strip() for line in open("../input/day11.txt", encoding="utf-8").readlines()]
empty_rows = [row for row, line in enumerate(lines) if all(ch=="." for ch in line)]
empty_cols = [col for col, line in enumerate(zip(*lines)) if all(ch=="." for ch in line)]
galaxies = [(row, col) for row, line in enumerate(lines) for col, ch in enumerate(line) if ch == "#"]

def calc(growth):
    dist = 0
    for (g1row, g1col), (g2row, g2col) in combinations(galaxies, 2):
        dist += abs(g1row - g2row) + abs(g1col - g2col)
        dist += sum([growth for r in empty_rows if min(g1row, g2row) < r < max(g1row, g2row)])
        dist += sum([growth for c in empty_cols if min(g1col, g2col) < c < max(g1col, g2col)])
    return dist

print(f"Answer A: {calc(1)}")
print(f"Answer B: {calc(999999)}")
