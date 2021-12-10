lines = [i.strip() for i in open("../input/day08.input", encoding="utf-8").readlines()]
A, B = 0, 0
for line in lines:
    patterns, outputs = line.split("|")
    twothreefive, zerosixnine, segments, wires = [], [], {}, {}

    for pattern in patterns.split():
        if len(pattern) == 2:
            segments[1] = ''.join(sorted(pattern))
        elif len(pattern) == 3:
            segments[7] = ''.join(sorted(pattern))
        elif len(pattern) == 4:
            segments[4] = ''.join(sorted(pattern))
        elif len(pattern) == 7:
            segments[8] = ''.join(sorted(pattern))
        elif len(pattern) == 5:
            twothreefive.append(''.join(sorted(pattern)))
        elif len(pattern) == 6:
            zerosixnine.append(''.join(sorted(pattern)))

    for s in zerosixnine:
        if not all(c in s for c in segments[1]):
            segments[6] = s
        elif all(c in s for c in segments[4]):
            segments[9] = s
        else:
            segments[0] = s

    for s in twothreefive:
        if all(c in s for c in segments[1]):
            segments[3] = s
        else:
            if len([c for c in segments[4] if c in s]) == 3:
                segments[5] = s
            else:
                segments[2] = s

    wires = {v: k for k, v in segments.items()}
    factor = 1000
    for output in [''.join(sorted(o)) for o in outputs.split()]:
        if len(output) in [2, 3, 4, 7]:
            A += 1
        B += factor * wires[output]
        factor //= 10

print("Answer A:", A)
print("Answer B:", B)
