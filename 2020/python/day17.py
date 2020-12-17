from collections import defaultdict
input = [line.strip() for line in open("../input/day17.input").readlines()]
D = [-1,0,1]
D = [(x,y,z,w) for x in D for y in D for z in D for w in D if not (x == 0 and y == 0 and z == 0 and w == 0)]

def processCube(C, lo, hi, use4D):
  Cnew = C.copy()
  for z in range(lo-1, hi + 2):
    for y in range(lo-1, hi + 2):
      for x in range(lo-1, hi + 2):
        for w in range(lo-1 if use4D else 0, hi + 3 if use4D else 1):
          n = len([True for dx,dy,dz,dw in D if C[(x + dx, y + dy, z + dz, w + dw )]])
          if C[(x,y,z,w)] and not 2 <= n <= 3: Cnew[(x,y,z,w)] = False
          elif not C[(x,y,z,w)] and n == 3: Cnew[(x,y,z,w)] = True
  return Cnew

def solve(use4D):
  C, lo, hi = defaultdict(bool), 0, len(input) - 1
  for y, line in enumerate(input):
    for x in range(len(line)): C[(x,y,0,0)] = True if line[x] == "#" else False
  for _ in range(6):
    C = processCube(C, lo, hi, use4D)
    lo -= 1
    hi += 1
  return len( [v for v in C.values() if v])

print("Answer A:", solve(False))
print("Answer B:", solve(True))
