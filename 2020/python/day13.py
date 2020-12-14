input = [line.strip() for line in open("../input/day13.input").readlines()]

T = int(input[0])
B = [int(b) for b in input[1].split(',') if b.isnumeric()]
minWait, minBus = 9999999999, 0

for b in B:
  dep = 0
  while dep < T: dep += b
  if dep < minWait:
    minWait = dep
    minBus = b
print("Answer A:", (minWait - T) * minBus)

B = [(int(b),i) for i, b in enumerate(input[1].split(',')) if b.isnumeric()] #list with modulos and remainders
# Chinese remainder theorem explanation: https://www.youtube.com/watch?v=zIFehsBHB8o
M = 1
for b in B: M *= b[0] # product of all modulos
bb = [(b[0] - b[1]) % b[0] for b in B] # remainders
Nb = [M // b[0] for b in B] # product of all modulos divided by current modulo
xb = [pow(Nb[i], B[i][0] - 2, B[i][0]) for i in range(len(B))] # inverse modulo, works because all modulos are prime numbers, otherwise see https://stackoverflow.com/a/9758173
bNxb = [bb[i] * Nb[i] * xb[i] for i in range(len(B))] #products of remainder, product of N and inverse modulo
print("Answer B:", sum(bNxb) % M) #lowest value that meets criteria
