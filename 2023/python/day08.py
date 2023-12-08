import math
instructions, mapping = [line for line in open("../input/day08.txt", encoding="utf-8").read().strip().split("\n\n")]
D = {k: (v.split(", ")[0][1:], v.split(", ")[1][:3])for k, v in [line.split(" = ") for line in mapping.split("\n")]}

def Navigate(pos, instructions, D, part2 = False):
    i, steps = 0, 0
    while (pos != "ZZZ" and not part2) or (not pos.endswith("Z") and part2):
        pos = D[pos][0] if instructions[i] == "L" else D[pos][1]
        i = (i + 1) % len(instructions)
        steps += 1
    return steps

print(f'Answer A: {Navigate("AAA", instructions, D)}')

positions = [x for x in D.keys() if x.endswith("A")]
cycles = [Navigate(pos, instructions, D, True) for pos in positions]
print(f"Answer B {math.lcm(*cycles)}")
