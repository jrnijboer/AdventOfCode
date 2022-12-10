c, X, A, B = 0, 1, {0: 1}, "\n"
for instr in [line.strip() for line in open("../input/day10.input", encoding="utf-8").readlines()]:
    for _ in range(1 if instr == "noop" else 2):
        B += "#" if (c % 40) - 1 <= X <= (c % 40) + 1 else " " + ("\n" if (c + 1) % 40 == 0 else "")
        c += 1
        A[c] = X
    if instr.startswith("addx"):
        X += int(instr.split()[1])

print("Answer A:", sum([k * v for k, v in A.items() if k in [20,60,100,140,180,220]]))
print(B)
