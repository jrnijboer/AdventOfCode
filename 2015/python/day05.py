from collections import Counter
lines = open("../input/day05.input", encoding="utf-8").readlines()

def isNiceA(s):
    ctr = Counter(s)
    if ctr['a'] + ctr['e'] + ctr['i'] + ctr['o'] + ctr['u'] < 3:
        return False

    hasDouble = False
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            hasDouble = True
            break
    if not hasDouble:
        return False

    for x in ["ab", "cd", "pq", "xy"]:
        if x in s:
            return False
    return True

def isNiceB(s):
    nice = False
    for i in range(len(s) - 2):
        ab = s[i] + s [i + 1]
        if ab in s[i + 2:]:
            nice = True
            break
    if not nice:
        return False

    for i in range(len(s) - 2):
        if s[i] == s[i + 2]:
            return True
    return False

A = B = 0
for line in lines:
    if isNiceA(line):
        A += 1
    if isNiceB(line):
        B += 1

print("Answer A:", A)
print("Answer B:", B)
