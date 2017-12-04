puzzleInput = 312051

#up, left, down, right
directions = [(0, 1), (-1, 0), (0, -1),(1, 0)]
#bootstrap the spiral
grid = { (0,0): 1, (1,0): 1, (1,1): 2 }
position = (1,1)
direction = 1

def move(pos):
    global direction
    grid
    newpos = map(sum, zip(pos, directions[direction % 4]))    
    neighbours = list()
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:            
            if ((newpos[0] + x, newpos[1] + y)) in grid:                
                neighbours.append(grid[(newpos[0] + x, newpos[1] + y)])    
    if len(neighbours) <= 2:
        direction += 1
        
    return (newpos[0], newpos[1]), sum(neighbours)

for _ in range(0,100):
    position, val = move(position)
    grid[position] = val
    if val > puzzleInput:
        print "now at {0}, value {1}".format(position, val)
        break
