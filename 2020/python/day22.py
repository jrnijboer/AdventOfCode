from collections import deque
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
    if tuple(A) in statesA and tuple(B) in statesB: return A + B, deque()
    statesA.add(tuple(A))
    statesB.add(tuple(B))
    a, b = A.popleft(), B.popleft()
    if recurse and a <= len(A) and b <= len(B):
      Asub, Bsub = play(deque(list(A)[:a]), deque(list(B)[:b]), recurse)
      A, B = appointCardsToWinner(A, B, a, b, 0 if len(Asub) > len(Bsub) else 1)
    else: A, B = appointCardsToWinner(A, B, a, b, 0 if a > b else 1)
  return A, B

A1, B1 = [deque(map(int, x.split("\n")[1:])) for x in [line.strip() for line in open("../input/day22.input").read().split("\n\n")]]
A2, B2 = [deque(map(int, x.split("\n")[1:])) for x in [line.strip() for line in open("../input/day22.input").read().split("\n\n")]]
A1, B1 = play(A1,B1, False)
print("Answer A:", sum([(len(A1) - i) * val for i, val in enumerate(A1)]) + sum([(len(B1) - i) * val for i, val in enumerate(B1)]))
A2, B2 = play(A2,B2, True)
print("Answer B:", sum([(len(A2) - i) * val for i, val in enumerate(A2)]) + sum([(len(B2) - i) * val for i, val in enumerate(B2)]))
