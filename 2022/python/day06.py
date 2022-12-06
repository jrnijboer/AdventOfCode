s = open("../input/day06.input", encoding="utf-8").read().strip()
A = True
for i, _ in enumerate(s):
    if A and len(set(s[i : i + 4])) == 4:
        print(f"Answer A: {i + 4}")
        A  = False
    if len(set(s[i : i + 14])) == 14:
        print(f"Answer B: {i + 14}")
        break
