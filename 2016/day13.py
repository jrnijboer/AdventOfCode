#http://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetTable
POPCOUNT_TABLE16 = [0] * 2**16
for index in xrange(len(POPCOUNT_TABLE16)):
	POPCOUNT_TABLE16[index] = (index & 1) + POPCOUNT_TABLE16[index >> 1]

def popcount32_table16(v):
	return (POPCOUNT_TABLE16[v & 0xffff] + POPCOUNT_TABLE16[(v >> 16) & 0xffff])

def getNextNodes(x, y):
	res = x * x + 3 * x + 2 * x * y + y + y * y + 1358 
	nextPositions = []
	if popcount32_table16(res) % 2 == 0:
		nextPositions = [[x + 1, y], [x, y + 1]]
		if x > 0:
			nextPositions.append([x - 1, y])
		if y > 0:
			nextPositions.append([x, y - 1])
	
	return nextPositions

nodes = [[1,1]]
moves = 0
count = 1 
visitedNodes = [[1,1]]
destinationFound = False
while not destinationFound:
	moves += 1
	newNodes = []
	for node in nodes:
		foundNodes = getNextNodes(node[0], node[1])
		for found in foundNodes:
			if found not in visitedNodes: 
				visitedNodes.append(found)
				newNodes.append(found)
				x = found[0]
				y = found[1]
				if popcount32_table16(x * x + 3 * x + 2 * x * y + y + y * y + 1358) % 2 == 0:
					count += 1
				if [31,39] in newNodes:
					destinationFound = True
					break
	nodes = newNodes
	if moves == 50:
		visitedNodes.sort()
		print 'visited locations after 50 moves:', count
print 'found destination in {} moves'.format(moves)
