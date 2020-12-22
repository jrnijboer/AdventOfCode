def play(D, recurse):
  A, B, seen = D[0], D[1], set()
  while A and B:
    if (tuple(A),tuple(B)) in seen: return [1], []
    seen.add((tuple(A), tuple(B)))
    a, b = A.pop(0), B.pop(0)
    if recurse and a <= len(A) and b <= len(B):
      Asub, Bsub = play([list(A)[:a], list(B)[:b]], recurse)
      D[0 if len(Asub) > len(Bsub) else 1].extend([a if len(Asub) > len(Bsub) else b, b if len(Asub) > len(Bsub) else a])
    else: D[0 if a > b else 1].extend([a if a > b else b, b if a > b else a])
  return [A, B]

A, B = [list(map(int, x.split("\n")[1:])) for x in [line.strip() for line in open("../input/day22.input").read().split("\n\n")]]
for i in range(2):
  D = play([A.copy(), B.copy()], i == 1)
  print(f"Answer {chr(65+i)}:", sum([(len(D[0]) - i) * val for i, val in enumerate(D[0])]) + sum([(len(D[1]) - i) * val for i, val in enumerate(D[1])]))
