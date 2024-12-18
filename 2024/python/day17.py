import re
input_registers, input_program = open("../input/17.txt", encoding="utf-8").read().split("\n\n")
input_program = list(map(int, re.findall(r"\d+", input_program)))
a, b, c = map(int, re.findall(r"\d+", input_registers))

def run(program, A, B, C):
    outbuff = []
    ip = 0
    while ip < len(program):
        opcode = program[ip]
        literal = program[ip + 1]
        combo = literal
        if literal == 4:
            combo = A
        elif literal == 5:
            combo = B
        elif literal == 6:
            combo = C
        if opcode == 0: # adv
            A = A//(2**combo)
        elif opcode == 1: # bxl
            B = B ^ literal
        elif opcode == 2: # bst
            B = combo % 8
        elif opcode == 3: # jnz
            if A != 0:
                ip = literal
                continue
        elif opcode == 4: # bxc
            B = B ^ C
        elif opcode == 5: # out
            outbuff.append(combo % 8)
        elif opcode == 6: #bdv
            B = A//(2**combo)
        elif opcode == 7: # cdv
            C = A//(2**combo)
        ip += 2
    return outbuff

candidates = [input_program[-1]]
for i in range(len(input_program)):
    next_candidates = []
    for val in candidates:
        for j in range(8):
            target = val * 8 + j
            if run(input_program, target, 0, 0) == input_program[-i-1:]:
                next_candidates.append(target)
        candidates = next_candidates

print("Answer A:", ",".join(str(d) for d in run(input_program, a, b, c)))
print("Answer B:", min(candidates))
