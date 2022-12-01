elves = sorted([sum([int(n) for n in group.split()]) for group in open("../input/day01.input", encoding="utf-8").read().split("\n\n")])
print(f"Answer A: {sum(elves[-1:])}")
print(f"Answer B: {sum(elves[-3:])}")
