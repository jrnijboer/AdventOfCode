direction  = 0 #N = 0, E = 1, S = 2, W = 3
directions = ["N", "E", "S", "W"]
steps = { 0: 0, 1: 0, 2: 0, 3: 0 }
with open("day1.input") as inputfile:
	instructions = inputfile.readline().split(',')

for instruction in instructions:
	instruction = instruction.strip()
	turn = instruction[0]
	stepcount = instruction[1:]
	if turn == "L":
		direction -= 1
	else:
		direction += 1
	direction %= 4
	steps[direction] += int(stepcount)

shortest = abs(steps[0] - steps[2]) + abs(steps[1] - steps[3])
print "shortest route is {}".format(shortest)

