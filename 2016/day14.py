import hashlib
triplets = {}
#salt = 'abc'
salt = 'zpqevtbw'
i = 0
found = 0
keys= []

def doTripleCheck(h, n):
	for i in range(30):
		if h[i] == h[i + 1] == h[i + 2]:
			if h[i] not in triplets or triplets[h[i]] < n - 1000:
				triplets[h[i]] = [n]
			else:
				triplets[h[i]].append(n)
			break

def getQuintuple(h):
	for i in range(28):
		if h[i] == h[i+1] == h[i+2] == h[i+3] == h[i+4]:
			return h[i]
	return ''

while found <= 64 :#and i < 1000:
	md5 = hashlib.md5()
	md5.update(salt+str(i))
	h = md5.hexdigest()
	#disable loop for part 1
	for _ in range(2016):
		h = hashlib.md5(h.encode('ascii')).hexdigest()
	doTripleCheck(h, i)
	char = getQuintuple(h)

	if char != '':
		#print 'quintuple found', i, char, h
		if char in triplets:
			for t in triplets[char]:
				if t < i and t + 1000 >= i:
					keys.append(t)
					found += 1
			triplets[char] = [i]
	i += 1
keys.sort()
print 'index', keys[63]

