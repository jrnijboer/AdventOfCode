with open("day5.input") as inputfile: instructionsA = [int(line[:-1]) for line in inputfile]
with open("day5.input") as inputfile: instructionsB = [int(line[:-1]) for line in inputfile]
def solve(instructions, B):
	steps = pos = 0
	while pos < len(instructions) and pos >= 0:
		x = 1 if instructions[pos] >= 3 and B else -1
		instructions[pos] += x * -1
		pos += instructions[pos] + x
		steps += 1
	return steps
print solve(instructionsA, False)
print solve(instructionsB, True)
