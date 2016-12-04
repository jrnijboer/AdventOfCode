import re
with open("day4.input") as inputfile:
	rooms = inputfile.readlines()

def decrypt(room, number):
	decrypted = ""
	for c in room:
		if c != '-':
			i =  ord(c) - 97
			i = ((i + number) % 26) + 97
			q = chr(i)
			decrypted += q
		else: decrypted += c
	return decrypted

for room in rooms:	
	pattern = '(.*)-(\d+)\[([a-z]+)\]'
	m = re.search(pattern, room)
	name = m.group(1)
	sectorid = int(m.group(2))
	if decrypt(name, sectorid) == "northpole-object-storage":
		print sectorid
		break
