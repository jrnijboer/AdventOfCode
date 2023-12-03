from collections import defaultdict
lines = ["." + line.strip() + "." for line in open("../input/day03.txt", encoding="utf-8").readlines()]
lines = ["." * (len(lines[0]) + 2)] + lines + ["." * (len(lines[0]) + 2)]
sumA, sumB, allGears, gears = 0, 0, defaultdict(list), set()

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
                                gears.add((lnr + dy, p + dx))
                if isPart:
                    sumA += int(number)
                    for g in gears:
                        allGears[g].append(int(number))
            gears, number = set(), ""
        pos += 1

print(f"Answer A: {sumA}")
sumB = sum([x[0] * x[1] for x in allGears.values() if (len(x) == 2)])
print(f"Answer B: {sumB}")
