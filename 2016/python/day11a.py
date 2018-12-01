import itertools
#Prometheum - A
#Cobalt - B
#Curicum - C
#Ruthenisum - D
#Plutonium - E
def getCombinations(source, dest, count):
	print 'source', source
	print 'dest', dest
	l = list(source)		
	d = list(dest)
	combinations = []
	
	for i in range(count):
		combination = [list(foo) for foo in itertools.combinations(l, i + 1)]
		combinations.extend(combination)
	print 'combinations:', combinations
	validCombinations = []
	hasDouble = False
	
	for c in combinations:
		d = list(dest)
		if len(c) == 2: hasDouble = True
		d.extend(c)
		d.sort()
		testState = ''.join(d)
		isValid = True

		for item in d[::-1]:
			if item < 'a':
				break
			if chr(ord(item) - 32)  not in d:
				isValid = False
				break
		if isValid and testState not in handledStates:
			validCombinations.append(testState)	
	
	if hasDouble:
		validCombinations = [c for c in validCombinations if len(c) == len(dest) + 2]
	print 'validcombinations: ', validCombinations
	return validCombinations

def getValidMoves(source, dest):
	sourcefloor = source[0]
	destfloor = dest[0]
	if sourcefloor < destfloor:
		validObjects = getCombinations(source[1:], dest[1:], 2)
	else:
		validObjects = getCombinations(source[1:], dest[1:], 1)		

	return validObjects 

def getStates(source, dest, moves):
	print 'moves', moves
	states = []
	for move in moves:
		s = source
		d = dest
		for obj in move:
			s = s.replace(obj, '')
			d = d + obj
		s = list(s)
s		s.sort()
		s = ''.join(s)
		d = list(d)
		d.sort()
		d = ''.join(d)
		states.append([s, d])
	print 'getstates', states
	return states		

def makeStateStringsUp(elevator, floordata, states):
	print 'floordata', floordata
	print 'states', states
	floordata.sort()
	nextStates = list()
	pre = str(elevator)
	post = ''
	for i in range(elevator - 2):
		print 'i', i
		print 'fldat', floordata[i]
		pre += floordata[i] + ':'
	print 'pre: ', pre
	for i in range(elevator + 1, 5):
		post += floordata[i-1] + ':'
	print 'post:', post
	for state in states:
		nextstate = pre + state[0] + ':' + state[1] + ':' + post
		nextStates.append(nextstate[:-1])
	return nextStates

def makeStateStringsDown(elevator, floordata, states):
	print 'floordatadown', floordata
	floordata.sort()
	nextStates = list()
	pre = str(elevator)
	post = ''
	for i in range(elevator - 1):
		print 'i', i
		print 'fldat', floordata[i]
		pre += floordata[i] + ':'
	print 'pre: ', pre
	for i in range(elevator + 2, 5):
		post += floordata[i-1] + ':'
	for state in states:
		nextstate = pre + state[1] + ':' + state[0] + ':' + post
		nextStates.append(nextstate[:-1])
	return nextStates

def getNextValidStates(state):
	nextStates = list()
	pos = int(state[0])
	floordata = state[1:].split(':')
	if pos < 4:#UP
		moves = getValidMoves(floordata[pos -1], floordata[pos])
		newStates = getStates(floordata[pos -1], floordata[pos], moves)
		nextStates.extend(makeStateStringsUp(pos + 1, floordata, newStates))
	
	if pos > 1:#DOWN
		moves = getValidMoves(floordata[pos - 1], floordata[pos - 2])
		newStates = getStates(floordata[pos - 1], floordata[pos - 2], moves)
		nextStates.extend(makeStateStringsDown(pos -1, floordata, newStates))
		
	return list(nextStates)

def processStates():
	global states

	nextstates = []
	moves += 1
	for state in states:
		validStates = getNextValidStates(state)
		nextstates.extend(validStates)
	
	states = nextstates


generators = { "A": 1, "B": 2, "C": 2, "D": 2, "E": 2 }

chips = { "a": 1, "b": 3, "c": 3, "d": 3, "e": 3 }
elevator = 1
moves = 0
states = set(['11Aa:2BCDE:3bcde:4'])
handledStates = []

#print getNextValidStates('11Aa:2BCDE:3bcde:4')
print 'startinput: 21Aa:2BCDE:3bcde:4'
print getNextValidStates('11Aa:2BCDE:3bcde:4')

#while '41:2:3:4ABCDEabcde' not in states:
#	processStates()
#	moves += 1

#print states

#if __name__ == "__main__":
#	main()
