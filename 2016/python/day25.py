import math
with open("day25.input.optimized") as inputfile:
	instructions = [line[:-1].split(' ') for line in inputfile]

def process(a):
	count = 0;
	pos = 0
	previous = '1'
	registers = { 'a': a, 'b': 0, 'c': 0, 'd': 0 }
	while pos < len(instructions):
		instruction = instructions[pos][0]
		args = instructions[pos][1:]	
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
			if args[0] == '0' and args[1] == '0':
				pos += 1
			elif (args[0] not in 'abcd' and args[0] != '0') or registers[args[0]] != 0:
				if args[1] not in 'abcd':
					pos += int(args[1])
				else:
					pos += registers[args[1]]
			else: 
				pos += 1
		elif instruction == 'tgl':
			offset = registers[args[0]]
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
		elif instruction == 'out':
			if registers[args[0]] != previous:
				if count == 20:
					print a
					exit()
				#print registers[args[0]]
				previous = registers[args[0]]
				pos += 1
				count += 1
			else:
				break
		elif instruction == 'add':
			registers[args[1]] += int(args[0])
			pos += 1
		else:
			print "Unknown instruction {0}".format(instruction)
			break

for a in range(0,1000):
	process(a)
