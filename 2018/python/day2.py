from collections import Counter
lines = sorted(open("../input/day2.input").readlines())
i, j = 0, 0
for line in lines:
    d = Counter(line)
    if 2 in d.values():
        i += 1
    if 3 in d.values():
        j += 1
print("day2, answer a:", i * j)

i, j = 0, 0
while True:
    diffs = 0
    s = ""
    for j in range(0, len(lines[i])):
        if lines[i][j] != lines[i+1][j]:
            diffs += 1
        else:
            s += lines[i][j]
    if diffs == 1:
        print("day2, answer b:", s)
        break
    i += 1

