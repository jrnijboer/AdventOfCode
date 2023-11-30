from itertools import combinations
containers = [int(line) for line in open("../2015/input/day17.input", encoding="utf-8").readlines()]
A, B = 0, []
for i in range(len(containers)):
    combs = [c for c in combinations(containers, i) if sum(c) == 150]
    A += len(combs)
    B = B + [len(c) for c in combs]
print("Answer A:", A)
print("Answer B:", len([b for b in B if b == min(B)]))
