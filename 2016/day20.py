with open("day20.input") as inputfile:
	blacklist = sorted([map (int, line[:-1].split('-')) for line in inputfile])
	available, lowest = 0, 0
	lowestFound = False
	for rule in blacklist:
		if rule[0] - lowest > 1:
			if not lowestFound:
				print 'lowest address found:', lowest + 1
				lowestFound = True
			available += -1 + rule[0] - lowest
		if lowest < rule[1]:
			lowest = rule[1]			
print 'total available:', available
