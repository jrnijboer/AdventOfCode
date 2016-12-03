def getNumber(instructions, number):	
	for direction in instructions:
		#print "going {}".format(direction)
		if direction == "R" and number % 3 != 0: number += 1
		elif direction == "U" and number > 3: number -= 3
		elif direction == "L" and number % 3 != 1: number -=1 
		elif direction == "D" and number < 7: number += 3
		#print "now at number {}".format(number)
	return number


with open("day2.input") as inputfile:
	instructions = inputfile.readlines()

lock = [[1,2,3],[4,5,6],[7,8,9]]

currentNumber = 5

for instruction in instructions:
	currentNumber = getNumber(instruction, currentNumber)
	print currentNumber
