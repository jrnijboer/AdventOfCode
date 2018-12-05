import re
lines = open("../input/day3.input").readlines()
claims = dict()

for line in lines:
    m = re.search('^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)
    id, left, top, width, height = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))
    for i in range(top, height + top):
        for j in range(left, width + left):
            if (i,j) in claims:
                claims[(i,j)].append(id)
            else:
                claims[(i,j)] = [id] 

overlapSize = 0
overlaps = set()
for key in claims:
    if len(claims[key]) > 1:
        overlapSize += 1
        for v in claims[key]:
            overlaps.add(v)

print("day3, answer a: ", overlapSize)
print("day3, answer b: ", (set(list(range(1, 1 + len(lines)))) - overlaps).pop())
