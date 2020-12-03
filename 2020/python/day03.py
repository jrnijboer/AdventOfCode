def trees(dx, dy, input):
  return len([(x,y) for x, y in [((y * dx // dy) % len(input[y]), y) for y in range(0, len(input), dy) ] if input[y][x] == "#"])

input = [line.strip() for line in open("../input/day03.input").readlines()]
print("Answer A:", trees(3, 1, input))
print("Answer B:", trees(1, 1, input) * trees(3, 1, input) * trees(5, 1, input) * trees(7, 1, input) * trees(1, 2, input))
