import itertools
input = [int(i.strip()) for i in open("../input/day01.input").readlines()]
print("Answer A:", [i[0] * i[1] for i in itertools.combinations(input, 2) if i[0] + i[1] == 2020][0])
print("Answer B:", [i[0] * i[1] * i[2] for i in itertools.combinations(input, 3) if i[0] + i[1] + i[2] == 2020][0])