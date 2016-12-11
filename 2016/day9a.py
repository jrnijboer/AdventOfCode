import re

def inflate(start, end):
	m = re.search('\((\d+)x(\d+)\)', compressed[start:end])
	return [int(m.group(1)) * int(m.group(2)), 1 + int(m.group(1))]

with open("day9.input") as inputfile:
	compressed = inputfile.read()

size = long(0)
pos = 0
end = len(compressed) - 1

while pos < end:
	if compressed[pos] == '(':
		start = pos
		while compressed[pos] != ')': pos += 1
		(sizeInc, posInc) = inflate(start, pos + 1)
		size += sizeInc
		pos += posInc 
	else:
		size += 1
		pos += 1

print size
