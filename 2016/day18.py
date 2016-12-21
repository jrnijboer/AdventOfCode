def getNextRow(row):
	row = '.' + row + '.'
	nextrow = ''
	pos = 1
	while pos < len(row) - 1:
		if (row[pos - 1] == '^' and row[pos] == '^' and row[pos + 1] == '.') or (row[pos - 1] == '.' and row[pos] == '^' and row[pos + 1] == '^') or (row[pos - 1] == '^' and row[pos] == '.' and row[pos + 1] == '.') or (row[pos - 1] == '.' and row[pos] == '.' and row[pos + 1] == '^'):
			nextrow += '^'
		else:
			nextrow += '.'
		pos += 1
	return nextrow


row = '.^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^.'
part1 = 40
part2 = 400000
index = 0
safe = 0
while index < part2:
	safe += row.count('.')
	if index == part1 - 1: 
		print 'part 1:', safe
	row = getNextRow(row)
	index += 1
print 'part 2:', safe
