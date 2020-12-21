input = [line.strip() for line in open("../input/day21.input").readlines()]
A, confirmedAllergens, I = {}, {}, {}

for line in input:
  for allergen in line.split("(")[1][len("contains "):-1].split(", "): A[allergen] = set()
  for i in line.split("(")[0][:-1].split(" "): I[i] = 1 if i not in I.keys() else I[i] + 1

for a in A.keys():
  A[a] = set(I.keys())
  for line in input:
    if a in line.split("(")[1][len("contains "):-1].split(", "):
      A[a] = A[a].intersection(set(line.split("(")[0][:-1].split(" ")))

while True:
  remove = [[k,v] for k, v in A.items() if len(v) == 1]
  if len(remove) > 0:
    confirmedAllergens[remove[0][0]] = list(remove[0][1])[0]
    del(A[remove[0][0]])
    for k in A.keys(): A[k] = A[k].difference(remove[0][1])
  else: break
print("Answer A:", sum([I[i] for i in set(I.keys()).difference(set(confirmedAllergens.values()))]))
print("Answer B:", ','.join([confirmedAllergens[k] for k in sorted(confirmedAllergens.keys())]))
