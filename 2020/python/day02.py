input = [line.replace("-", " ").replace(":", "").split(" ") for line in open("../input/day02.input").readlines()]
print("Answer A:", len([t for t in input if int(t[0]) <= t[3].count(t[2]) <= int(t[1])]))
print("Answer B:", len([t for t in input if (t[3][int(t[0]) - 1 ] == t[2]) != (t[3][int(t[1]) - 1 ] == t[2])]))
