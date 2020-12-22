def appointCardsToWinner(D, a, b, winner):
  D[winner].append(a if winner == 0 else b)
  D[winner].append(b if winner == 0 else a)
  return D

def play(D, recurse):
  A, B, statesA, statesB = D[0], D[1], set(), set()
  while A and B:
    if tuple(A) in statesA and tuple(B) in statesB: return [1], []
    statesA.add(tuple(A))
    statesB.add(tuple(B))
    a, b = A.pop(0), B.pop(0)
    if recurse and a <= len(A) and b <= len(B):
      Asub, Bsub = play([list(A)[:a], list(B)[:b]], recurse)
      D = appointCardsToWinner(D, a, b, 0 if len(Asub) > len(Bsub) else 1)
    else: D = appointCardsToWinner(D, a, b, 0 if a > b else 1)
  return [A, B]

A, B = [list(map(int, x.split("\n")[1:])) for x in [line.strip() for line in open("../input/day22.input").read().split("\n\n")]]
D = play([A.copy(),B.copy()], False)
print("Answer A:", sum([(len(D[0]) - i) * val for i, val in enumerate(D[0])]) + sum([(len(D[1]) - i) * val for i, val in enumerate(D[1])]))
D = play([A,B], True)
print("Answer B:", sum([(len(D[0]) - i) * val for i, val in enumerate(D[0])]) + sum([(len(D[1]) - i) * val for i, val in enumerate(D[1])]))
