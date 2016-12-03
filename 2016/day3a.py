with open("day3.input") as inputfile:
	inputlines = inputfile.readlines()
validTriangles = 0

for line in inputlines:
	items = sorted([int(s) for s in line.split() if s.isdigit()], key = int)
	if items[0] + items[1] > items[2]:
		validTriangles += 1

print validTriangles
