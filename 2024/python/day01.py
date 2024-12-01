lines = [line.strip().split("   ") for line in open("../input/01.txt", encoding="utf-8").readlines()]
left = sorted([int(line[0]) for line in lines])
right = sorted([int(line[1]) for line in lines])
print("Answer A:", sum([abs(l - r) for l, r in zip(left, right)]))
print("Answer B:", sum( i * right.count(i) for i in left))
