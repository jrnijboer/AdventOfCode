from functools import reduce
input = [part.strip() for part in open("../input/day16.input").read().split("\n\n")]
fields = input[0]
myticket = [int(i) for i in input[1].split("\n")[1].split(",")]
nearby = [list(map(int,t.split(","))) for t in input[2].split("\n")[1:]]
partA, rules = 0, {}

def isValid(ticket, rules):
  for value in ticket:
    valid = False
    for r in rules.keys():
      if value in rules[r]: valid = True
    if not valid: return value
  return 0

#build dictionary of field:set of valid numbers
for line in fields.split("\n"):
  field, ranges = line.split(":")
  rules[field] = set()
  for minmaxRange in ranges[1:].split(" or "):
    min, max = map(int, minmaxRange.split("-"))
    rules[field] = rules[field].union(set([i for i in range(min, max + 1)]))

#filter valid tickets
validTickets = []
for ticket in nearby:
  e = isValid(ticket, rules)
  if e == 0:
    validTickets.append(ticket)
  partA += e
print("Answer A:", partA)

#for all fields, check possible indexes
fields = rules.keys()
positions = {f:[] for f in fields}
for f in fields:
  for i in range(len(fields)):
    valid = 0
    for v in validTickets:
      if v[i] in rules[f]: valid += 1
    if valid == len(validTickets):
      positions[f] += [i]

#sort and then remove index from fields to the right where current field only has index
sortedpositions = sorted([(k,v) for k, v in positions.items()], key = lambda x:len(x[1]))
for i in range(len(sortedpositions)-1):
  for j in range(i+1, len(sortedpositions)):
    sortedpositions[j][1].remove(sortedpositions[i][1][0])

print("Answer B:", reduce(lambda x, y: x * y, [myticket[p[1][0]] for p in sortedpositions if p[0].startswith("departure")], 1))
