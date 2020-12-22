def appointCardsToWinner(A, B, a, b, winner):
  if winner == 0:
    A.append(a)
    A.append(b)
  else:
    B.append(b)
    B.append(a)
  return A, B

def play(A, B, recurse):
  statesA, statesB = set(), set()
  while A and B:
    if tuple(A) in statesA and tuple(B) in statesB: return [1], []
    statesA.add(tuple(A))
    statesB.add(tuple(B))
    a, b = A.pop(0), B.pop(0)
    if recurse and a <= len(A) and b <= len(B):
      Asub, Bsub = play(list(A)[:a], list(B)[:b], recurse)
      A, B = appointCardsToWinner(A, B, a, b, 0 if len(Asub) > len(Bsub) else 1)
    else: A, B = appointCardsToWinner(A, B, a, b, 0 if a > b else 1)
  return A, B

A, B = [list(map(int, x.split("\n")[1:])) for x in [line.strip() for line in open("../input/day22.input").read().split("\n\n")]]
A1, B1 = play(A.copy(),B.copy(), False)
print("Answer A:", sum([(len(A1) - i) * val for i, val in enumerate(A1)]) + sum([(len(B1) - i) * val for i, val in enumerate(B1)]))
A2, B2 = play(A,B, True)
print("Answer B:", sum([(len(A2) - i) * val for i, val in enumerate(A2)]) + sum([(len(B2) - i) * val for i, val in enumerate(B2)]))
