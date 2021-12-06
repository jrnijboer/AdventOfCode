lines = [i.strip() for i in open("../input/day02.input", encoding="utf-8").readlines()]
D = {"forward": 1j, "down": 1, "up": -1}

pos = sum([D[line.split()[0]] * int(line.split()[1]) for line in lines])
print("Answer A:", int(pos.imag * pos.real))

x, y, aim = 0, 0, 0
for direction, steps in [line.split() for line in lines]:
    if direction == "forward":
        x += int(steps)
        y += aim * int(steps)
    else:
        aim += int(steps) * D[direction]
print("Answer B:", x * y)
