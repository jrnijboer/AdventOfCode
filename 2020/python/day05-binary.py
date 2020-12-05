seats = [int(line.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2) for line in open("../input/day05.input").readlines()]
print("Answer A:", max(seats))
print("Answer B:", int ((min(seats) + max(seats)) / 2 *  (1 + len(seats))) - sum(seats))
