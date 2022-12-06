from collections import Counter
A, B = 0, 0
bags = [line.strip() for line in open("../input/day03.input", encoding="utf-8").readlines()]
for i, bag in enumerate(bags):
    for c in set(Counter(bag[:len(bag) // 2])).intersection(Counter(bag[len(bag) // 2:])):
        A += ord(c) - 96 if c.islower() else ord(c) - 38
    if i % 3 == 0:
        for c in set(Counter(bag)).intersection(Counter(bags[i + 1])).intersection(Counter(bags[ i + 2])):
            B += ord(c) - 96 if c.islower() else ord(c) - 38

print(f"Answer A: {A}")
print(f"Answer B: {B}")
