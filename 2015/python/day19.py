import collections
parts = open("../2015/input/day19.input", encoding="utf-8").read().split("\n\n")
replacements = [part.split(" => ") for part in parts[0].split("\n")]
target = str(parts[1]).strip()

A = set()
for replacement in replacements:
    pos = target.find(replacement[0])
    while pos > 0:
        molecule = target[:pos] + replacement[1] + target[pos + len(replacement[0]):]
        A.add(molecule)
        pos = target.find(replacement[0], pos + 1)
print("Answer A:", len(A))

startElement = target[::-1]
pos = 0
elementlist = []

while pos < len(startElement):
    if startElement[pos] >= 'a' and startElement[pos] <= 'z':
        elementlist += [startElement[pos: pos + 2][::-1]]
        pos += 1
    else:
        elementlist += [startElement[pos]]
    pos += 1
y_elements = len([e for e in elementlist if e == "Y"])
rn_ar_elements = len([e for e in elementlist if e in ["Ar", "Rn"]])

print("Answer B:", len(elementlist) - rn_ar_elements - (2 * y_elements) - 1)
