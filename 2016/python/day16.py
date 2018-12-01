def applyCurve(s):
	return s + '0' + s[::-1].replace('0', 'x').replace('1', '0').replace('x', '1')

def createChecksum(s):
	result = ''	
	for pair in [s[i:i+2] for i in range(0,len(s), 2)]:
		if pair[0] == pair[1]: result += '1'
		else: result += '0'
	if len(result) % 2 == 0: return createChecksum(result)	
	else: return result

#part 1
l = 272
state = '01000100010010111'
while len(state) <= l:
	state = applyCurve(state)
print 'part 1:', createChecksum(state[:l])

#part 2
l = 35651584
state = '01000100010010111'
while len(state) <= l:
	state = applyCurve(state)
print 'part 2:', createChecksum(state[:l])

