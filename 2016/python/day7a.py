from collections import Counter

with open("day7.input") as inputfile:
	ips = [ip[:-1] for ip in inputfile]

validCount = 0
for ip in ips:
	isValidIP = False
	inHypernetSequence = False
	for pos in range(0, len(ip) - 3):		
		if ip[pos] == '[': inHypernetSequence = True
		elif ip[pos] == ']': inHypernetSequence = False
		if inHypernetSequence:
			if ip[pos] == ip[pos+3] and ip[pos+1] == ip[pos+2]:
				isValidIP = False
				break
		else:
			if ip[pos] == ip[pos+3] and ip[pos+1] == ip[pos+2] and ip[pos] != ip[pos +1]:
				isValidIP = True
	if isValidIP:
		validCount += 1

print validCount


