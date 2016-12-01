direction  = 0 #N = 0, E = 1, S = 2, W = 3
directions = ["N", "E", "S", "W"]
steps = { 0: 0, 1: 0, 2: 0, 3: 0 }
x = 0
y = 0

xd = 0
yd = 1

locations = ["0,0"]

with open("day1.input") as inputfile:
	instructions = inputfile.readline().split(',')

found = False
for instruction in instructions:
	instruction = instruction.strip()
	turn = instruction[0]
	stepcount = instruction[1:]
	if turn == "L":
		direction -= 1
	else:
		direction += 1
	direction %= 4
	stepcount = int(stepcount)
	steps[direction] += stepcount
	if direction == 0:
		xd = 0
		yd = 1
	elif direction == 1:
		xd = 1
		yd = 0
	elif direction == 2:
		xd = 0
		yd = -1
	else:
		xd = -1
		yd = 0
	
	while stepcount > 0:
		x += xd
		y += yd
		location = "{},{}".format(x,y)
		if location in locations:
			print "{} is already visited".format(location)
			found = True
			break
		locations.append(location)
		stepcount -= 1
	if found:
		break

shortest = abs(x) + abs(y)
print "shortest route to first visited location is {}".format(shortest)

