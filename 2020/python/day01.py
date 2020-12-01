import itertools
input = [int(i.strip()) for i in open("../input/day01.input").readlines()]
print("Answer A:", [i * j for i, j in itertools.combinations(input, 2) if i + j == 2020][0])
print("Answer B:", [i * j * k for i, j, k in itertools.combinations(input, 3) if i + j + k == 2020][0])
