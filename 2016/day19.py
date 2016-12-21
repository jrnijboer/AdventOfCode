import math
def getWinnerPart1(i):
	p = int(math.log(i, 2))
	return i - (2 ** (p + 1) - 1 - i)

elves = 3012210
print 'part 1:', getWinnerPart1(elves)

def getWinnerPart2(i):
	#serie returns powers of 3 
	#resets to 0 and increments by 1 till halfway next power of 3, increments by 2 for 2nd half

	exp = int(math.log(i,3))
	p = 3 ** exp 
	if i == p:
		return i
	nextP = 3 ** (exp + 1)
	offsetfromp = i - p 
	halfway = (nextP - p) / 2
	if offsetfromp <= halfway:
		return offsetfromp
	
	return offsetfromp + (offsetfromp - halfway) 

print 'part 2:', getWinnerPart2(elves)

	
