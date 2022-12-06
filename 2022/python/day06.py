s = open("../input/day06.input", encoding="utf-8").read().strip()
A = True
for i, _ in enumerate(s):
    if len(set([s[i], s[i+1], s[i+2], s[i+3]])) == 4 and A:
        print(f"Answer A: {i + 4}")
        A  = False
    if len(set([s[i], s[i+1], s[i+2], s[i+3], s[i+4], s[i+5], s[i+6], s[i+7], s[i+8], s[i+9], s[i+10], s[i+11], s[i+12], s[i+13]])) == 14:
        print(f"Answer B: {i + 14}")
        break
