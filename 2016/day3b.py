with open("day3.input") as inputfile:
	inputlines = inputfile.readlines()
validTriangles = 0

def checkCol(items, index):
	lengths = sorted([items[index], items[index + 1], items[index + 2]], key = int)
	if lengths[0] + lengths[1] > lengths[2]:
		return 1
	return 0

colA = []
colB = []
colC = []

for line in inputlines:
	numbers = [int(s) for s in line.split() if s.isdigit()]
	colA.append(numbers[0])
	colB.append(numbers[1])
	colC.append(numbers[2])

count = len(colA)

for i in range(0, count, 3):	
	validTriangles += checkCol(colA, i)
	validTriangles += checkCol(colB, i)
	validTriangles += checkCol(colC, i)

print validTriangles
	
