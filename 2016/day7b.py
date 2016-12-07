from collections import Counter

with open("day7.input") as inputfile:
	ips = [ip[:-1] for ip in inputfile]

validCount = 0
for ip in ips:
	isValidIP = False
	start = 0
	net = ''
	supernets = []
	hypernets = []
	for pos in range(0, len(ip)):
		if ip[pos]  ==  '[':
			supernets.append(net)
			net = ''
		elif ip[pos] == ']':
			hypernets.append(net)
			net = ''
		else: net += ip[pos]
	supernets.append(net)

	for supernet in supernets:
		for pos in range(0, len(supernet) - 2):
			if supernet[pos] == supernet[pos+2]:
				aba = supernet[pos:pos+3]
			
				bab = supernet[pos+1] + supernet[pos] + supernet[pos+1]
				for hypernet in hypernets:
					if bab in hypernet:					
						isValidIP = True
						break
			if isValidIP: break
		if isValidIP: break

	if isValidIP:
		validCount += 1

print validCount


