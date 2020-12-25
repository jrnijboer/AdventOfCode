input, black_tiles = [line.strip() for line in open("../input/day24.input").readlines()], set()
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
  if pos in black_tiles: black_tiles.remove(pos)
  else: black_tiles.add(pos)
print("Answer A:", len(black_tiles))

for _ in range(100):
  neighbours = [2 + 0j, -2 + 0j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j]
  NEW, check = black_tiles.copy(), black_tiles.copy()
  for p in black_tiles:
    for neighbour in neighbours: check.add(p + neighbour)
  for p in check:
    n = 0
    for neighbour in neighbours:
      if p + neighbour in black_tiles: n += 1
    if p in black_tiles and (n == 0 or n > 2): NEW.remove(p)
    elif p not in black_tiles and n == 2:  NEW.add(p)
  black_tiles = NEW
print("Answer B:", len(black_tiles))
