from collections import defaultdict
lines = ["." + line.strip() + "." for line in open("../input/day03.txt", encoding="utf-8").readlines()]
lines = ["." * (len(lines[0]) + 2)] + lines + ["." * (len(lines[0]) + 2)]
sumA, sumB, allGears = 0, 0, defaultdict(set)

for lnr, line in enumerate(lines):
    pos, number = 0, ""
    while pos < len(line):
        if line[pos].isdigit():
            number += line[pos]
        else:
            if number != "":
                isPart = False
                for p in range(pos - len(number), pos):
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if not lines[lnr + dy][p + dx].isdigit() and lines[lnr + dy][p + dx] != ".":
                                isPart = True
                            if lines[lnr + dy][p + dx] == "*":
                                allGears[(lnr + dy, p + dx)].add(int(number))
                if isPart:
                    sumA += int(number)
            number = ""
        pos += 1

print(f"Answer A: {sumA}")
sumB = sum([n[0] * n[1] for n in [list(x) for x in allGears.values() if (len(x) == 2)]])
print(f"Answer B: {sumB}")
