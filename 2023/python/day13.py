patterns = [line.split("\n") for line in open("../input/day13.txt", encoding="utf-8").read().strip().split("\n\n")]

def isMirrorOnColumn(pattern, allowedErrors=0):
    for i in range(1, len(pattern[0])):
        errors = 0
        for row in pattern:
            left = row[:i][::-1]
            right = row[i:]
            if not left.startswith(right) and not right.startswith(left):
                errors += 1
        if errors == allowedErrors:
            return i
    return 0

def isMirrorOnRow(pattern, allowedErrors=0):
    for i in range(len(pattern) - 1):
        errors = 0
        for col in range(len(pattern[0])):
            up = "".join([pattern[j][col] for j in range(i, -1, -1)])
            down = "".join([pattern[j][col] for j in range(i+1, len(pattern))])
            if not up.startswith(down) and not down.startswith(up):
                errors += 1
        if errors == allowedErrors:
            return i + 1
    return 0

scoreA, scoreB = 0, 0
for pattern in patterns:
    scoreA += isMirrorOnRow(pattern, 0) * 100 + isMirrorOnColumn(pattern, 0)
    scoreB += isMirrorOnRow(pattern, 1) * 100 + isMirrorOnColumn(pattern, 1)

print(scoreA)
print(scoreB)