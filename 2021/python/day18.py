from typing import Tuple
from itertools import permutations

def reduceSnail(snail: list) -> list:
    keepReducing = True
    while keepReducing:
        keepReducing, snail = explode(snail)
        if keepReducing:
            continue
        keepReducing, snail = splitSnail(snail)
    return snail

def explode(snail: list) -> Tuple[bool, list]:
    for idx, tpl in enumerate(snail):
        depth, value = tpl
        if depth >= 4:
            if idx > 0:
                snail[idx - 1] = (snail[idx - 1][0], snail[idx - 1][1] + value)
            if idx < len(snail) - 2:
                snail[idx + 2] = (snail[idx + 2][0], snail[idx + 2][1] + snail[idx + 1][1])
            del snail[idx + 1]
            snail[idx] = (depth - 1, 0)
            return True, snail
    return False, snail

def splitSnail(snail: list) -> Tuple[bool, list]:
    for idx, tpl in enumerate(snail):
        depth, value = tpl
        if value >= 10:
            snail[idx] = (depth + 1, value // 2)
            snail.insert(idx + 1, (depth + 1, (value + 1) // 2))
            return True, snail
    return False, snail

def makeSnail(line: str) -> list:
    snail, depth = [], -1
    for c in line:
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
        elif c.isdigit():
            snail.append((depth, int(c)))
    return snail

def addSnail(s1: list, s2: list) -> list:
    for i in range(len(s1)):
        s1[i] = (s1[i][0] + 1, s1[i][1])
    for i in range(len(s2)):
        s2[i] = (s2[i][0] + 1, s2[i][1])
    return s1 + s2

# def calcMagnitude(snail: list) -> int:
#     deepest = max([pair[0] for pair in snail])
#     while deepest != 0:
#         for idx, pair in enumerate(snail):
#             depth = pair[0]
#             if depth == deepest:
#                 del snail[idx]
#                 snail[idx] = (depth - 1, 3 * pair[1] + 2 * snail[idx][1])
#         deepest = max([pair[0] for pair in snail])
#     return 3 * snail[0][1] + 2 * snail[1][1]

def calcMagnitude(snail: list) -> int:
    while len(snail) > 1:
        deepest = max([pair[0] for pair in snail])
        for idx, pair in enumerate(snail):
            depth = pair[0]
            if depth == deepest:
                del snail[idx]
                snail[idx] = (depth - 1, 3 * pair[1] + 2 * snail[idx][1])
    return snail[0][1]

lines = [line.strip() for line in open("../input/day18.input", encoding="utf-8").readlines()]
snail = makeSnail(lines[0])
for line in lines[1:]:
    nextSnail = makeSnail(line)
    snail = reduceSnail(addSnail(snail, nextSnail))
print("Answer A:", calcMagnitude(snail))

B = 0
for a, b in list(permutations(range(len(lines)), 2)):
    snail = addSnail(makeSnail(lines[a]), makeSnail(lines[b]))
    B = max(calcMagnitude(reduceSnail(snail)), B)
print("Answer B:", B)
