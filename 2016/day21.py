import re
import itertools
def doSwap(s, command):
	m = re.search('^swap letter (\w) with letter (\w)$', command) 
	if m is not None:
		return swap(s, m.group(1), m.group(2))
	else:
		m = re.search('^swap position (\d) with position (\d)$', command)
		return swapByPos(s, int(m.group(1)), int(m.group(2)))

def doRotate(s, command):
	m = re.search('^rotate (left|right) (\d) step', command)
	if m is not None:
		if m.group(1) == 'left': direction = -1
		else: direction = 1
		return rotateByDirection(s, direction, int(m.group(2)))
	else:
		m = re.search('^rotate based on position of letter (\w)$', command)
		return rotateByChar(s, m.group(1))

def doReverse(s, command):
	m = re.search('^reverse positions (\d) through (\d)$', command)
	return reverse(s, int(m.group(1)), int(m.group(2)))

def doMove(s, command):
	m = re.search('^move position (\w) to position (\w)$', command)
	return move(s, int(m.group(1)), int(m.group(2)))

def swapByPos(s, a, b):
	s = list(s)
	x = s[a]
	s[a] = s[b]
	s[b] = x
	return ''.join(s)

def swap(s, a, b):
	if not a.isdigit():
		for i in range(0, len(s)):
			if s[i] == a:
				a = i
				break
	
	if not b.isdigit():
		for i in range(0, len(s)):
			if s[i] == b:
				b = i
				break
	
	return swapByPos(s, a, b)


def reverse(s, start, end):
	s = list(s)
	rev = []
	last = []
	rev.extend(s[:start])
	rev.extend(s[start:end + 1][::-1])
	if end < len(s) - 1:
		rev.extend(s[end + 1:])
	return ''.join(rev)

def move(s, a, b):
	'starting move with', s
	s = list(s)
	x = s[a]
	del(s[a])
	m = s[:b]
	m.extend(x)
	m.extend(s[b:len(s)])

	return ''.join(m)


def rotateByDirection(s, direction, steps):
	if direction > 0:
		steps 
		rot = s[len(s) - steps:] + s[:len(s) - steps ] 
		return rot
	if direction < 0:
		rot = s[steps:] + s[:steps]
		return rot 
	return s
	
def rotateByChar(s, char):
	steps = 1 
	for i in range(0, len(s)):
		if s[i] == char:
			steps += i
			if i >= 4: 
				steps += 1
			break
	s = rotateByDirection(s, 1, steps)
	return s

with open("day21.input") as inputfile:
	commands = [line[:-1] for line in inputfile]

s = 'abcdefgh'
for command in commands:
	if command.startswith('swap'):
		s = doSwap(s, command)
	elif command.startswith('rotate'):
		s = doRotate(s, command)
	elif command.startswith('reverse'):
		s = doReverse(s, command)
	elif command.startswith('move'):
		s = doMove(s, command)
	else:
		print 'error'
print 'part 1:', s

candidates = [list(foo) for foo in itertools.permutations('abcdefgh', 8)]
for candidate in candidates:
	s = candidate
	for command in commands:
		if command.startswith('swap'):
			s = doSwap(s, command)
		elif command.startswith('rotate'):
			s = doRotate(s, command)
		elif command.startswith('reverse'):
			s = doReverse(s, command)
		elif command.startswith('move'):
			s = doMove(s, command)
	if s == 'fbgdceah':
		print 'part 2:', ''.join(candidate)
		break
