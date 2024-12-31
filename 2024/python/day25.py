data = open("../input/25.txt", encoding="utf-8").read().split("\n\n")
keys, locks = [], []

for i, pattern in enumerate(data):
    lines = pattern.strip().split("\n")
    if lines[0].startswith("#"):
        locks.append(i)
    else:
        keys.append(i)
A = sum(all(all(char1 != "#" or char2 != "#" for char1, char2 in zip(line1, line2))
    for line1, line2 in zip(data[i], data[k]))
    for i in keys
    for k in locks)

print("Answer A:", A)
