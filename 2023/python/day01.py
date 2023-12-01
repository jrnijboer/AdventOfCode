lines = [line.strip() for line in open("../input/day01.txt", encoding="utf-8").readlines()]
sumA, sumB = 0, 0
NumberDict = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e", "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}

for line in lines:
    sumA += int([i for i in line if i.isdigit()][0] + [i for i in line if i.isdigit()][-1])
    for k, v in NumberDict.items():
        line = line.replace(k, v)
    sumB += int([i for i in line if i.isdigit()][0] + [i for i in line if i.isdigit()][-1])

print(f"Answer A: {sumA}")
print(f"Answer B: {sumB}")
