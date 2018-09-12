import re

with open("day9.input") as inputfile:
	compressed = inputfile.read()

def inflate(s, factor):
	print "{} time inflating: {} ".format(factor,s)
	pos = 0
	size = 0
	while pos < len(s):
		m = re.search('^\((\d+)x(\d+)\)', s[pos:])
		if m is not None:
			chars = int(m.group(1))
			repeats = int(m.group(2))
			l = len(m.group(0))
			print "match for chars:", chars, "repeats", repeats
			
			size += inflate(s[pos + len(m.group(0)):pos + len(m.group(0)) + int(m.group(1))] , int(m.group(2)))
			pos += len(m.group(0)) + int(m.group(1)) - 1
			print "continue from", pos
		else:
			size += 1
			#print 'next'

		pos += 1

	print "returning size", size * factor
	return size * factor


size = long(0)
pos = 0
end = len(compressed) - 1

size = inflate(compressed[:-1], 1)

#			m = re.search('\((\d+)x(\d+)\)', s[start:pos + 1])
print size
