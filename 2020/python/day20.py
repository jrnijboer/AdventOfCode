import copy
from collections import defaultdict
data = [line.strip() for line in open("../input/day20.input").read().split("\n\n")]

def flip(image):
  return [image[y][::-1] for y in range(len(image))]

def rotate(image):
  newImage = copy.deepcopy(image)
  for y in range(len(image)):
    for x in range(len(image[y]) ):
      newImage[x][len(image)-1 - y] = image[y][x]
  return newImage

def getAllPermutations(image):
  data = [[c for c in s] for s in image]
  r1 = data
  f1 = flip(copy.deepcopy(r1))
  r2 = rotate(r1)
  f2 = flip(copy.deepcopy(r2))
  r3 = rotate(r2)
  f3 = flip(copy.deepcopy(r3))
  r4 = rotate(r3)
  f4 = flip(copy.deepcopy(r4))
  return [r1,r2,r3,r4,f1,f2,f3,f4]

def getBorders(images):
  return [''.join(image[0]) for image in images]

def getPermutation(permutations, border, direction):
  for perm in permutations:
    if border == getBorderFromImage(perm, direction): return perm

def getBorderFromImage(image, direction):
  if direction == "R":   return ''.join([image[y][len(image) -1] for y in range(len(image))])
  elif direction == "L": return ''.join([image[y][0] for y in range(len(image))])
  elif direction == "U": return ''.join(image[0])
  elif direction == "D": return ''.join(image[len(image)-1])

def isMonster(image, x, y):
  monster = [(0,18), (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19), (2,1), (2,4), (2,7), (2,10), (2,13), (2,16)]
  found = True
  for m in monster:
    my,mx = m[0], m[1]
    if image[(x +mx, y+my )] != "#": return False
  return found
#get permutations and border for each image
S, sizeS, partA = {}, 0, 1
for square in data:
  lines = square.split("\n")
  id = int(lines[0].split(" ")[1][:-1])
  permutations = getAllPermutations(lines[1:])
  borders = getBorders(permutations)
  neighbours = []
  S[id] = [permutations, borders, neighbours, {}, []]
#find neighbouring images
squares = list(S.keys())
for i in range(len(squares)):
  for j in range(i +1, len(squares)):
    for b in S[squares[i]][1]:
      if b in S[squares[j]][1]:
        S[squares[i]][2].append(squares[j])
        S[squares[i]][3][squares[j]] = b
        S[squares[j]][2].append(squares[i])
        S[squares[j]][3][squares[i]] = b
        break
for k, v in S.items():
  if len(v[2]) == 2:
    partA *= k
    corner = k
print("Answer A:", partA)

#setup upperleft corner
G, Gid = {}, {}
permutations = S[corner][0]
neighbours = list(S[corner][3].items())
correctOrientedPerm = getPermutation(permutations, neighbours[0][1], "R")
bottomOrientedPerm = getPermutation(permutations, neighbours[1][1], "D")
if ''.join(correctOrientedPerm[0]) != ''.join(bottomOrientedPerm[0]):
  #fix orientation to build starting from upperleft
  correctOrientedPerm = rotate(correctOrientedPerm)
  correctOrientedPerm = rotate(correctOrientedPerm)
  correctOrientedPerm = flip(correctOrientedPerm)
G[(0,0)] = correctOrientedPerm
Gid[(0,0)] = corner
nextId = neighbours[0][0]
nextBorder = neighbours[0][1]

while sizeS * sizeS != len(S): sizeS += 1
#loop until grid complete
for row in range(sizeS):
  for column in range(sizeS):
    if row == 0 and column == 0: continue
    permutations = S[nextId][0]
    correctOrientedPerm = getPermutation(permutations, nextBorder, "L") if column != 0 else getPermutation(permutations, nextBorder, "U")
    G[(row, column)] = correctOrientedPerm
    Gid[(row, column)] = nextId
    if column < sizeS -1:
      nextBorder = getBorderFromImage(correctOrientedPerm, "R")
      neighbours = S[nextId][3]
    else:
      nextBorder = getBorderFromImage(G[(row, 0)], "D")
      neighbours = S[Gid[(row, 0)]][3]
    for k,v in neighbours.items():
      if v == nextBorder or v == nextBorder[::-1]:
        nextId = k
#trim minigrids
Grid = {k : [ line[1:-1] for line in  [''.join(s) for s in [''.join(row) for row in v]][1:-1]] for k, v in G.items()}

#create full grid from minigrids
FullGrid = {k: "" for k in range(sizeS * len(Grid[(0,0)]))}
for y in range(sizeS):
  for x in range(sizeS):
    innerGrid = Grid[y,x]
    for yy in range(len(innerGrid)):
      FullGrid[y * len(innerGrid) + yy] += innerGrid[yy]

#create all full permutations
fullImage = [[c for c in s] for s in FullGrid.values()]
fullPermutations = getAllPermutations(fullImage)

#build 8 dictionaries from full permutations
FD = []
for p in fullPermutations:
  d = defaultdict(str)
  arr = [''.join(r) for r in p]
  for y in range(len(arr)):
    for x in range(len(arr[0])):
      d[(x,y)] = arr[y][x]
  FD.append(d)

#find monsters in all dictionaries
monsters = 0
for y in FullGrid.keys():
  for x in FullGrid.keys():
    for d in FD:
      if isMonster(d, x, y):
        monsters += 1
print("Answer B:", len([v for v in FD[0].values() if v == "#"]) - monsters * 15)
