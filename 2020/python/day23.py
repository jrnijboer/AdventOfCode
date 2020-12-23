def playGame(partB=False):
  input = [int(c) for c in "368195742"]
  if partB: input.extend(range(10,1000001))
  current, dest, C = input[0], 0, {input[i]:input[i+1] for i in range(len(input) - 1)}
  C[input[-1]] = input[0]

  for _ in range(100 if not partB else 10000000):
    picks, p = [], current #start rule 1: pick 3 cups
    for i in range(3):
      p = C[p]
      picks.append(p)
    C[current] = C[p] #fix the link after yanking out the 3 cups

    dest = current - 1 if current > 1 else len(input) #start rule 2: select destination
    while dest in picks:
      dest -= 1
      if dest <= 0: dest = len(input)

    tmp = C[dest] #start rule 3: place cups
    for pick in picks:
      C[dest] = pick
      dest = pick
    C[dest] = tmp

    current = C[current] #start rule 4 begin: select next current cup
  return C

C = playGame()
partA, x = "", 1
for _ in range(8):
  partA += str(C[x])
  x = C[x]
print("Answer A:", partA)

C = playGame(True)
print("Answer B:", C[1] * C[C[1]])
