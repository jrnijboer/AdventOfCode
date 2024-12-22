from collections import defaultdict
digits = list(map(int, open("../input/22.txt", encoding="utf-8").read().strip().split("\n")))
A, B = 0, defaultdict(int)

for digit in digits:
    prev = digit % 10
    s1, s2, s3, s4 = -10, -10, -10, -10
    seen = set()
    for _ in range(2000):
        digit = ((digit * 64) ^ digit) % 16777216
        digit = ((digit // 32) ^ digit) % 16777216
        digit = ((digit * 2048) ^ digit) % 16777216
        diff = digit % 10 - prev
        prev = digit % 10
        s1, s2, s3, s4 = s2, s3, s4, diff
        if (s1, s2, s3, s4) not in seen:
            seen.add((s1, s2, s3, s4))
            B[(s1, s2, s3, s4)] += digit % 10
    A += digit

print("Answer A:", A)
print("Answer B:", max(B.values()))
