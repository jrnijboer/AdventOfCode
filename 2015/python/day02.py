lines = open("../input/day02.input").readlines()
A, B = 0, 0

for line in lines:
    l, w, h = [ int(i) for i in line.split('x')]
    A += 2 * l * w + 2 * w * h + 2 * h * l + min([l * w, w * h, h * l])
    B += sum(sorted([l, w, h])[:2]) * 2 + l * w * h

print(f"Answer A: {A}")
print(f"Answer B: {B}")
