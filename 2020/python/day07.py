input = [line.strip() for line in open("../input/day07.input").readlines()]
goldcarriers, added, bags, bagcount = [], 1, {}, 0
for line in input:
  if not "bags contain no" in line:
    contents = line[8 + line.index("contain "):].split(", ")
    bags[line[:line.index(" bags")].replace(" ", "")] = [(int(x[0]), x[1] + x[2]) for x in [c.split(" ") for c in contents]]

while(added > 0):
  added = 0
  for key, values in bags.items():
    for v in values:
      if (v[1] == 'shinygold' or v[1] in goldcarriers) and key not in goldcarriers:
        goldcarriers.append(key)
        added += 1
print("Answer A:", len(goldcarriers))

Q = [(1, 'shinygold')]
while (len(Q) > 0):
  bag = Q.pop()
  bagcount += bag[0]
  if bag[1] in bags.keys():
    for x in bags[bag[1]]:
      Q.append((bag[0] * x[0], x[1]))
print("Answer B:", bagcount - 1)
