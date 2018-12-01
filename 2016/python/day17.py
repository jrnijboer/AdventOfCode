import hashlib

def getNextStates(state):
	s = state[0]
	x,y = state[1]
	possibleStates = []
	md5 = hashlib.md5()
	md5.update(s)
	h = md5.hexdigest()
	if h[:1] in 'bcdef' and y > 0: possibleStates.append([s+'U', [x, y - 1]])
	if h[1:2] in 'bcdef' and y < 3: possibleStates.append([s+'D', [x, y + 1]])
	if h[2:3] in 'bcdef' and x > 0: possibleStates.append([s+'L', [x - 1, y]])
	if h[3:4] in 'bcdef' and x < 3: possibleStates.append([s+'R', [x + 1, y]])
	
	return possibleStates

passcode = 'njfxhljp'
found = False
states = [[passcode, [0, 0]]]
moves = 0
maxroute = 0
while len(states) > 0:
	nextStates = []
	for state in states:
		if state[1] == [3,3]:
			if not found:
				print 'part 1:', state[0][len(passcode):]
				found = True
			maxroute = moves
			continue
		nextStates.extend(getNextStates(state))
	moves += 1
	states = nextStates
print 'part 2:', maxroute
