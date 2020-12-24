from collections import defaultdict
input, G = [line.strip() for line in open("../input/day24.input").readlines()], defaultdict(bool)
for line in input:
  line, ix, pos = line.replace("ne", "A").replace("nw", "B").replace("se", "C").replace("sw", "D"),  0, 0 + 0j
  while ix < len(line):
    if line[ix] == "e": pos += 2 + 0j
    elif line[ix] == "w": pos -= 2 + 0j
    elif line[ix] == "A": pos += 1 + 1j
    elif line[ix] == "B": pos += -1 + 1j
    elif line[ix] == "C": pos += 1 - 1j
    elif line[ix] == "D": pos += -1 - 1j
    ix += 1
  G[pos] = not G[pos]
print("Answer A:", len([v for v in G.values() if v]))

for _ in range(100):
  neighbours, keys = [2 + 0j, -2 + 0j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j], list(G.keys())
  for k in keys:
    for n in neighbours: G[k + n] = G[k + n]
  Gnext = G.copy()
  for tile in G.keys():
    n = len([1 for pos in neighbours if tile + pos in G.keys() and G[tile + pos]])
    if (n not in [1, 2] and G[tile]) or (n == 2 and not G[tile]): Gnext[tile] = not G[tile]
  G = Gnext
print("Answer B:", len([v for v in G.values() if v]))
