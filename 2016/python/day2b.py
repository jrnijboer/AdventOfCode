keypad = [['-', '-', '1', '-', '-'],['-','2', '3', '4', '-'],['5','6', '7', '8', '9'],['-','A', 'B', 'C', '-'],['-','-', 'D', '-', '-']]

x = 0
y = 2

def getNumber(instructions, x, y):
	for direction in instructions:
		if direction == "R" and x < 4 and keypad[y][x+1] != '-': x += 1 
		elif direction == "U" and y >= 1 and keypad[y-1][x] != '-':	y -= 1
		elif direction == "L" and x >= 1 and keypad[y][x-1] != '-':	x -= 1
		elif direction == "D" and y < 4 and keypad[y+1][x] != '-': y += 1
	return (x,y)


with open("day2.input") as inputfile:
	instructions = inputfile.readlines()

currentPos = keypad[y][x]

code = ""
for instruction in instructions:
	(x,y) = getNumber(instruction, x, y)
	code += keypad[y][x]

print code
