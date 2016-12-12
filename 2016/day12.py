with open("day12.input") as inputfile:
	instructions = inputfile.readlines()

pos = 0

#part 1:
#registers = { 'a': 123, 'b': 0, 'c': 0, 'd': 0 }

#part 2:
registers = { 'a': 123, 'b': 0, 'c': 1, 'd': 0 }

while pos < len(instructions):
	instruction = instructions[pos]
	parts = instruction[:-1].split(' ')
	if parts[0] == ('cpy'):
		if parts[1].isdigit():
			registers[parts[2]] = int(parts[1])
		else:
			registers[parts[2]] = registers[parts[1]]
		pos += 1
	elif parts[0] == 'inc':
		registers[parts[1]] += 1
		pos += 1
	elif parts[0] == 'dec':
		registers[parts[1]] -= 1
		pos += 1
	elif parts[0] == 'jnz':
		if (parts[1].isdigit() and parts[1] != '0') or registers[parts[1]] != 0:
			pos += int(parts[2])
		else: 
			pos += 1
print registers['a']
