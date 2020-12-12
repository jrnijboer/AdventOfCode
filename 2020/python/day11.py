def fillSeats(n, directylyAdjacent):
  deltas = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
  seats = [list(line.strip()) for line in open("../input/day11.input").readlines()]
  changes, width, height = None, len(seats[0]), len(seats)
  while changes == None or len(changes) > 0:
    changes = []
    for y in range(height):
      for x in range(width):
        hasNeighbours, neighbours = False, 0
        for dx, dy in deltas:
          d1, d2 = dx, dy
          while not directylyAdjacent and 0 <= x + dx < width and 0 <= y + dy < height and seats[y+dy][x+dx] == ".":
            dx += d1
            dy += d2
          if seats[y][x] == "L":
            if 0 <= x + dx < width and 0 <= y + dy < height and seats[y + dy][x + dx] == "#":
              hasNeighbours = True
              break
          if seats[y][x] == "#" and 0 <= x + dx < width and 0 <= y + dy < height and seats[y + dy][x + dx] == "#": neighbours += 1
        if seats[y][x] == "L" and not hasNeighbours: changes.append((x, y, "#"))
        if seats[y][x] == "#" and neighbours >= n: changes.append((x, y, "L"))
    for x, y, val in changes: seats[y][x] = val
  return len([(x,y) for x in range(len(seats[y])) for y in range(len(seats)) if seats[y][x] == "#" ])

print("Answer A:", fillSeats(4, True))
print("Answer B:", fillSeats(5, False))
