import itertools
with open("day24.input") as inputfile :    maze = [line[:-1] for line in inputfile]

def calcDistance(start, destination):
	visited = [start]
	queue = [(0, start)]
	for distance, (row, col) in queue:
		if (row,col) == destination:
			return distance
		for rowNext, colNext in ((row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)):
			if maze[rowNext][colNext] != '#' and (rowNext, colNext) not in visited:
				visited.append((rowNext, colNext))
				queue.append((distance + 1, (rowNext, colNext)))

nodes = dict()
for y, row in enumerate(maze):
	for x, location in enumerate(row):
		if location.isdigit():
			nodes[location] = (int(y),int(x))
			if location == '0':
				start = [0, (y,x)]

distances = {}
for src in nodes:
	for dest in nodes:
		if src < dest:
			distances[int(src), int(dest)] = distances[int(dest),int(src)] = calcDistance(nodes[src], nodes[dest])

def calcRoute(mustReturn):
	shortest = 2000000000
	for r in list(itertools.permutations(range(1,len(nodes)))):
		route = (0,) + r
		if mustReturn:
			route = route + (0,)
		step = 0 
		current = 0
		while current < shortest and step < (len(route) - 1):
			current += distances[(route[step],route[step+1])]
			step += 1;
		if current < shortest:
			shortest = current
	return shortest

print calcRoute(False)
print calcRoute(True)
