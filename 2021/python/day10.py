def checkCorruption(s: str):
    S = []
    for c in s:
        if c in "{[(<":
            S.append(c)
        elif abs(ord(c) - ord(S[-1])) <= 2:
            S.pop()
        else:
            return True, [c]
    return False, S

errorScores = {")": 3, "]": 57, "}": 1197, ">": 25137}
lines = [i.strip() for i in open("../input/day10.input", encoding="utf-8").readlines()]
errors, B = [], []

for chunk in lines:
    err, res = checkCorruption(chunk)
    if err:
        errors.append(res[0])
    else:
        score = 0
        for r in res[::-1]:
            score = score * 5 + "([{<".find(r) + 1
        B.append(score)
print("Answer A:", sum(errorScores[e] for e in errors))
print("Answer B:", list(sorted(B))[len(B) // 2])
