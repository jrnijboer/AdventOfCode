import re
import time

def fillRectangle(command):
	pattern = '^rect (\d+)x(\d+)$'	
	m = re.search(pattern, command)
	x = int(m.group(1))
	y = int(m.group(2))
	for i in range(y):
		for j in range(x):
			grid[i][j] = True

def printGrid(line):
	print (chr(27) + "[2J")
	print line
	print
	print '01234567890123456789012345678901234567890123456789'
	lights = 0
	for i in range(ySize):
		line = ''
		for j in range(xSize):
			if grid[i][j] == True: 
				line += '#'
				lights += 1
			else: line += '-'
		print line
	print '{} lights are on'.format(lights)

def rotate(command):
	pattern = '^rotate (row|column) (y|x)=(\d+) by (\d+)'
	m = re.search(pattern, command)
	q = int(m.group(3))
	count = int(m.group(4))
	if m.group(1) == 'row': rotateRow(q, count)
	else: rotateColumn(q, count)

def rotateRow(row, count):
	currentRow = grid[row]
	newRow = []
	for i in range(xSize):
		pos = (xSize - count) + i
		newRow.append(currentRow[pos % xSize])
	grid[row] = newRow
	
def rotateColumn(column, count):
	currentColumn = []
	for i in range(ySize):
		currentColumn.append(grid[i][column])

	newColumn = []
	for i in range(ySize):
		pos = (ySize - count) + i
		newColumn.append(currentColumn[pos % ySize])
	
	for i in range(ySize):
		grid[i][column] = newColumn[i]
	
xSize = 50 
ySize = 6

grid = []

with open("day8.input") as inputfile:
	lines = [line[:-1] for line in inputfile]

for y in range(ySize):
	line = []
	for x in range(xSize): line.append(False)
	grid.append(line)

for line in lines:
	if line.startswith('rect'):
		fillRectangle(line)
	else:
		rotate(line)
	printGrid(line)
	time.sleep(0.2)
