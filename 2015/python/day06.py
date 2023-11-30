import re
lines = open("../input/day06.input", encoding="utf-8").readlines()
pattern = "^(.*) (\d+),(\d+) through (\d+),(\d+)"
A, B = [], []

for x in range(1000):
    A.append([])
    B.append([])
    for y in range(1000):
        A[x].append(0)
        B[x].append(0)

for line in lines:
    cmd, x1, y1, x2, y2 = re.match(pattern, line).groups()
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

    if cmd == "toggle":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                A[x][y] = 1 - A[x][y]
                B[x][y] += 2
    elif cmd == "turn off":
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                A[x][y] = 0
                B[x][y] = max(B[x][y] -1, 0)
    else:
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                A[x][y] = 1
                B[x][y] += 1

print("Answer A:", sum(sum(l) for l in A))
print("Answer B:", sum(sum(l) for l in B))
