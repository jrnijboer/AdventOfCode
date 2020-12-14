from collections import defaultdict
input = [line.strip() for line in open("../input/day14.input").readlines()]
Mem, Mem2, Mask = defaultdict(int), defaultdict(str), ""

def applyMaskA(val, mask):
  return int(''.join([val[i] if mask[i] == 'X' else mask[i] for i in range(36)]), 2)

def applyMaskB(val, mask):
  return ''.join([ val[i] if mask[i] == "0" else mask[i] for i in range(36)])

def getDestinations(v):
  V = [v]
  while "X" in V[0]:
    v = V.pop(0)
    pos = v.index("X")
    s = [c for c in v]
    s[pos] = "0"
    V.append(''.join(s))
    s[pos] = "1"
    V.append(''.join(s))
  return [int(v,2) for v in V]

for line in input:
  if line.startswith("mask"):
    Mask = line.split(" = ")[1]
  else:
    m = int(line[line.index("[")+1:line.index("]")])
    val = int(line.split(" = ")[1])
    binvalA = bin(val)[2:].zfill(36)
    Mem[m] = applyMaskA(binvalA, Mask)
    binvalB = bin(m)[2:].zfill(36)
    for d in getDestinations(applyMaskB(binvalB, Mask)): Mem2[d] = val
print("Answer A:", sum(Mem.values()))
print("Answer B:", sum(Mem2.values()))
