from collections import defaultdict
patterns = [line.split(",") for line in open("../input/day15.txt", encoding="utf-8").read().strip().split("\n")][0]
boxes = defaultdict(dict)

def hash(s, val=0):
    return val if s == "" else hash(s[1:], ((val + ord(s[0])) * 17) % 256)

for pattern in patterns:
    if pattern.endswith("-"):
        boxes[hash(pattern[:-1])].pop(pattern[:-1], 0)
    else:
        id, focal = pattern.split("=")
        boxes[hash(id)][id] = int(focal)

print("Answer A:", sum(map(hash, patterns)))
print("Answer B:", sum([(k + 1) * (id + 1) * val for k, v in boxes.items() for id, val in enumerate(v.values())]))
