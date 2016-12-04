import re
with open("day4.input") as inputfile:
	rooms = inputfile.readlines()

sumSectors = 0

def isRealRoom(room, checksum):
	letters = {}
	for c in room:
		if c != '-' and c in letters:
			letters[c] += 1
		elif c!= '-':
			letters[c] = 1	
	return checksumFromDict(letters) == checksum

def checksumFromDict(letters):
	letters = sorted(letters.items(), key = lambda x: (x[1] * -1, x[0]))[0:5]
	return ''.join([letter[0] for letter in letters])

for room in rooms:	
	pattern = '(.*)-(\d+)\[([a-z]+)\]'
	m = re.search(pattern, room)
	name = m.group(1)
	sectorid = int(m.group(2))
	checksum = m.group(3)
	if isRealRoom(name, checksum):
		sumSectors += sectorid 

print sumSectors
	
