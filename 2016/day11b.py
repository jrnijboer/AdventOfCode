import itertools

def getDoubleCombinations(source, dest):
	#print 'source', source
	#print 'dest', dest
	l = list(source)		
	combinations = [list(foo) for foo in itertools.combinations(l, 2)]
	#print 'combinations:', combinations
	validCombinations = []
	
	for c in combinations:
		#print 'testing combination', c

		d = list(dest)
		d.extend(c)
		d.sort()	
		newSource = source.replace(c[0],'').replace(c[1],'')
		newDest = ''.join(d)
		
		#print 'testing states', newDest, newSource
		if stateIsValid(newDest) and stateIsValid(newSource):
			validCombinations.append([newSource,newDest])
		else:
			#print 'the combination {} is not valid'.format(c)
			pass
	
	#print 'validDoublecombinations: ', validCombinations
	return validCombinations

def stateIsValid(state):
	#test empty
	if len(state) == 0:
		return True
	#test lowers have uppers
	if state[0] <= 'Z':
		for lower in state[::-1]:
			if lower < 'a':
				break
			if chr(ord(lower) - 32) not in state:
				#print state, 'is not valid'
				return False
	return True

def getSingleCombinations(source, dest):
	#print 'source', source
	#print 'dest', dest
	validCombinations = []
	
	for c in source:
		d = list(dest)
		d.append(c)
		d.sort()
		newSource = source.replace(c,"")
		newDest = ''.join(d)
		if stateIsValid(newDest) and stateIsValid(newSource):
			validCombinations.append([newSource, newDest])
				
	#print 'validSingleCombinations', validCombinations
	return validCombinations

def doValidMoves(source, dest):
	#print 'doing moves from', source
	#print 'to', dest
	sourcefloor = source[0]
	destfloor = dest[0]
	#if sourcefloor < destfloor:
	#print 'calc UP'
	validObjects = getDoubleCombinations(source[1:], dest[1:])
	#if len(validObjects) == 0:
	validObjects.extend(getSingleCombinations(source[1:], dest[1:]))
	#else:
		#print 'calc DOWN'
	#	validObjects = getDoubleCombinations(source[1:], dest[1:])
#		if len(validObjects) == 0:
#			validObjects = (getSingleCombinations(source[1:], dest[1:]))
	return validObjects 

def getNextValidStates(state):
	#print 'incoming state', state
	nextStates = list()
	minpos = int(state[0])
	pos = int(state[1])
	floordata = state[2:].split(':')
	#print 'floordata', floordata
	if pos < 4:#UP
		newminpos = 1
		upstates = doValidMoves(floordata[pos -1], floordata[pos])
		#print 'upstates', upstates
		pre = str(pos + 1) 		
		for i in range(pos -1):
			pre += floordata[i] + ':'
		
		#print 'pre:', pre
		post = ''
		for i in range(pos + 1, 4):
			post += floordata[i] + ':'			 
		#print 'post:', post

		#print 'upstates', upstates  
		for s in upstates:			
			n = pre + str(pos) + s[0] + ':' + str(pos + 1) + s[1] + ':' + post
			parts = n[1:].split(':')
			minfloor=0
			while len(parts[minfloor]) == 1:
				minfloor += 1
			n = str(minfloor + 1) + n
			#print 'next up state:', n
			nextStates.append(n[:-1])
	
	if pos > 1:# and pos > minpos :#DOWN
		downstates = doValidMoves(floordata[pos - 1], floordata[pos - 2])
		#print downstates
		pre = str(minpos) + str(pos - 1)
		for i in range(pos - 2):
			pre += floordata[i] + ':'
		#print 'down pre:', pre
		post = ''
		for i in range(pos, 4):
			post += floordata[i] + ':'
		#print 'post:', post

		#print 'downstates: ', downstates
		for s in downstates:
			n = pre + str(pos - 1) + s[1] + ':' + str(pos) + s[0] + ':' + post
			#print 'next down state:', n
			nextStates.append(n[:-1])
		 		
	return nextStates

def processStates():
	#part1
	#states = ['111Aa:2BCDE:3bcde:4']
	#endstate = '441:2:3:4ABCDEabcde'
	
	#part2
	states = ['111AFGafg:2BCDE:3bcde:4']
	endstate = '441:2:3:4ABCDEFBabcdefg'

	#endstate = '441:2:3:4ABab'
	#states = ['111ab:2A:3B:4']
	found = False
	moves = 0
	calculations = 0
	handledStates = dict()

	while not found:
		if len(states) == 0:
			print 'no more valid states to process'
			break
		moves += 1
		print 'starting move', moves, ', possible states to calculate', len(states)
		print 'handled states so far', len(handledStates)
		nextstates = []
		for state in states:
			if state not in handledStates:
				handledStates[state] = moves
				calculations += 1
				#print 'processing', state
				validStates = getNextValidStates(state)
				nextstates.extend(validStates)
				#print validStates
				if endstate == state:
					found = True
					print 'found endstate in {} moves'.format(moves)
					print 'calculated {} states'.format(calculations)
					break
			else:
				#print 'filtered out', state
				pass
			#print 'returned with', validStates
			#print 
		states = nextstates
	#print handledStates

#print getNextValidStates('331:2:3ABCDEabcde:4')
processStates()
