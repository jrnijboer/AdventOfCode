import math
with open("day23.input") as inputfile:
	instructions = [line[:-1].split(' ') for line in inputfile]



#print instructions
pos = 0

#part 1:
registers = { 'a': 8, 'b': 0, 'c': 0, 'd': 0 }

#part 2:
#a! + 5840
#registers = { 'a': 123, 'b': 0, 'c': 1, 'd': 0 }
def toggle(target):
	#print 'target', target
	if target >=0 and target < len(instructions):
		#print 'toggle instruction', instructions[target], 'pos argument:', target
		if len(instructions[target]) == 2:
			if instructions[target][0] == 'inc':
				instructions[target][0] = 'dec'
			else:
				instructions[target][0] = 'inc'
		else:
			if instructions[target][0] == 'jnz':
				instructions[target][0] = 'cpy'
			else:
				instructions[target][0] = 'jnz'


while pos < len(instructions):
	#print instructions[pos]
	#print 'register value', registers['a'], registers['b'], registers['c'], registers['d']
	instruction = instructions[pos][0]
	args = instructions[pos][1:]	
	#print 'instruction', instruction, 'arguments', args
	if instruction == ('cpy'):
		if args[0] not in 'abcd':
			registers[args[1]] = int(args[0])
		else:
			registers[args[1]] = registers[args[0]]
		pos += 1
	elif instruction == 'inc':
		registers[args[0]] += 1
		pos += 1
	elif instruction == 'dec':
		registers[args[0]] -= 1
		pos += 1
	elif instruction == 'jnz':
		if (args[0] not in 'abcd' and args[0] != '0') or registers[args[0]] != 0:
			if args[1] not in 'abcd':
				pos += int(args[1])
			else:
				pos += registers[args[1]]
		else: 
			pos += 1
	elif instruction == 'tgl':
		offset = registers[args[0]]
		#print 'offset:', offset, 'pos', pos
		if offset + pos >= 0 and offset + pos <= len(instructions):
			toggle(pos + offset)
		pos += 1
	elif instruction == 'noop':
		pos += 1
	elif instruction == 'fact':
		f = math.factorial(registers['d'])
		registers['a'] = int(f)
		registers['b'] = 2
		registers['c'] = 0
		registers['d'] = 1
		pos += 1
print registers['a']
