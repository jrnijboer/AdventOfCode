lines = open("../input/day07.input", encoding="utf-8").readlines()
wires = {}

def getValue(w):
    if w in cache:
        return cache[w]
    elif w.isnumeric():
        return int(w)
    elif wires[w].isnumeric():
        return int(wires[w])
    else:
        if 'AND' in wires[w]:
            w1, _, w2 = wires[w].split()
            result = getValue(w1) & getValue(w2)
        elif 'LSHIFT' in wires[w]:
            src, _, val = wires[w].split()
            result = getValue(src) << getValue(val)
        elif 'NOT' in wires[w]:
            _, src = wires[w].split()
            result = 65535 - getValue(src)
        elif 'OR' in wires[w]:
            w1, _, w2 = wires[w].split()
            result = getValue(w1) | getValue(w2)
        elif 'RSHIFT' in wires[w]:
            src, _, val = wires[w].split()
            result = getValue(src) >> getValue(val)
        else:
            result = getValue(wires[w])
        cache[w] = result
    return cache[w]

for line in [l.strip() for l in lines]:
    val, w = line.split(" -> ")
    wires[w] = val

cache = {}

print("Answer A:", getValue('a'))

cache = {}
cache['b'] = 16076
print("Answer B:", getValue('a'))
