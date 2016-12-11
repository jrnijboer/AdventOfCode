import re

instructions = dict()
bots = dict() 
outputs = dict()

def AddBotValues(bot, value):
	bot.append(value)
	bot.sort()
	return bot[:2]

def DoBotInstruction(key):
	instr = instructions[key]
	m = re.search('^\s*low to (.*?) (\d+) and high to (.*?) (\d+)$', instr)
	if m.group(1) == 'bot':
		destKey = int(m.group(2))
		if destKey in bots:
			bots[destKey] = AddBotValues(bots[destKey], bots[key][0])
		else:
			bots[destKey] = [bots[key][0]]
	else:
		outputs[int(m.group(2))] = bots[key][0]
	if m.group(3) == 'bot':
		destKey = int(m.group(4))
		if destKey in bots:
			bots[destKey] = AddBotValues(bots[destKey], bots[key][1])
		else:
			bots[destKey] = [bots[key][1]]
	else:
		outputs[int(m.group(4))] = bots[key][1]
	bots[key] = []

with open("day10.input") as inputfile:
	for line in inputfile:
		m = re.search('^value (\d+) goes to bot (\d+)$', line)
		if m is not None:
			id  = int(m.group(2)) 
			if id in bots:
				bots[id] = AddBotValues(bots[id], int(m.group(1)))
			else:
				bots[id] = [int(m.group(1))]		
		else: 
			m = re.search('^bot (\d+) gives(.*)', line[:-1])
			instructions[int(m.group(1))] = m.group(2)
canRun = True
while canRun:
	canRun = False
	for key in bots.copy():
		if 17 in bots[key] and 61 in bots[key]:
			print "found bot with chips 17 and 61:", key
		if len(bots[key]) == 2:
			DoBotInstruction(key)
			canRun = True
print "product of outputs 1,2,3: ", outputs[0] * outputs[1]* outputs[2]
