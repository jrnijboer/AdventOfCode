from collections import defaultdict
F = defaultdict(int)
for n in open("../input/day06.input", encoding="utf-8").read().strip().split(","):
    F[int(n)] += 1

for day in range(256):
    new, FNext = F[0], {i: F[(i + 1) % 9] for i in range(9)}
    FNext[6] += new
    F = FNext
    if day + 1 == 80:
        print("Answer A:", sum(F.values()))
print("Answer B:", sum(F.values()))
