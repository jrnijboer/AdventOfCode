from collections import defaultdict
from itertools import combinations
G = [list(line.strip()) for line in open("../input/08.txt", encoding="utf-8")]
antennas = defaultdict(list)
for y, row in enumerate(G):
    for x, char in enumerate(row):
        if char != ".":
            antennas[char].append((x, y))

def solve(partA):
    hashes = set()
    for v in antennas.values():
        for a, b in combinations(v, 2):
            dx, dy = b[0] - a[0], b[1] - a[1]
            scale = 1 if partA else 0
            while True:
                dxx, dyy = dx * scale, dy * scale
                additions = 0
                if 0 <= a[0] - dxx < len(G[0]) and 0 <= a[1] - dyy < len(G):
                    hashes.add((a[0] - dxx, a[1] - dyy))
                    additions += 1
                if 0 <= b[0] + dxx < len(G[0]) and 0 <= b[1] + dyy < len(G):
                    hashes.add((b[0] + dxx, b[1] + dyy))
                    additions += 1
                if additions == 0 or partA:
                    break
                scale += 1
    return len(hashes)

print("Answer A:", solve(True))
print("Answer B:", solve(False))
