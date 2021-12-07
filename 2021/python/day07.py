from statistics import median, mean
from math import floor, ceil

N = [int(i.strip()) for i in open("../input/day07.input", encoding="utf-8").read().split(",")]
print("Answer A:", sum(abs(n - int(median(N))) for n in N))

X = [floor(mean(N)), ceil(mean(N))]
print("Answer B:", min(sum(abs(x - n) * (abs(x - n) + 1) // 2 for n in N) for x in X))
