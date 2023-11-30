lines = [line.strip() for line in open("../2015/input/day16.input", encoding="utf-8").readlines()]

for idx, line in enumerate(lines):
    parts = line.split(':', 1)[1].split(',')
    auntA, auntB = True, True
    for part in parts:
        k, v = part.split(':')
        k = k.strip()
        v = int(v)
        if (k == "children" and v == 3) or (k == "cars" and v == 2) or (k == "perfumes" and v == 1) \
        or (k == "samoyeds" and v == 2) or (k == "akitas" and v == 0) or (k == "vizslas" and v == 0):
            continue
        if not ((k == "cats" and v == 7) or (k == "pomeranians" and v == 3)  or (k == "goldfish" and v == 5) or (k == "trees" and v == 3)):
            auntA = False
        if not ((k == "cats" and v > 7) or (k == "pomeranians" and v < 3) or (k == "goldfish" and v < 5) or (k == "trees" and v > 3)):
            auntB = False
    if auntA:
        print("Answer A:", idx + 1)
    if auntB:
        print("Answer B:", idx + 1)
