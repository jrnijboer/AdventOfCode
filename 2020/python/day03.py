input = [line.strip() for line in open("../input/day03.input").readlines()]
vectors = [(1,1), (3,1), (5,1), (7,1), (1,2)]
b = 1
for vector in vectors:
  trees, x = 0, 0
  for y in range(0, len(input), vector[1]):
    if input[y][x] == "#": trees += 1
    x = (x + vector[0]) % len(input[y])
  if vector == (3,1): print("Answer A:", trees)
  b *= trees
print("Answer B:", b)