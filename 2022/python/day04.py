lines = [line.strip().replace("-", ",") for line in open("../input/day04.input").readlines()]
A, B = 0, 0
for line in lines:
    a1, a2, b1, b2 = [int(c) for c in line.split(",")]
    if a1 <= b1 and a2 >= b2 or b1 <= a1 and b2 >= a2:
        A += 1
    B += 0 if a2 < b1 or b2 < a1 else 1

print(f"Answer A: {A}")
print(f"Answer B: {B}")
