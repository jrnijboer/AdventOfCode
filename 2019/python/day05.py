def solve(inputValue):
    instructions = list(map(int,open("../input/day5.input").readline().split(",")))
    opcode, ip, val1, val2 = instructions[0], 0, 0, 0
    while opcode != 99:
        m1, m2= instructions[ip] % 1000 // 100, instructions[ip] % 10000 // 1000
        if opcode != 3 and opcode != 4:
            val1 = instructions[ip + 1] if m1 == 1 else instructions[instructions[ip + 1]]
            val2 = instructions[ip + 2] if m2 == 1 else instructions[instructions[ip + 2]]
        if opcode == 1: instructions[instructions[ip + 3]] = val1 + val2
        elif opcode == 2: instructions[instructions[ip + 3]] = val1 * val2
        elif opcode == 3: instructions[instructions[ip + 1]] = inputValue
        elif opcode == 4:
            s = instructions[ip + 1] if m1 == 1 else instructions[instructions[ip + 1]]
            if s != 0: return (s)
        elif opcode == 5: ip = val2 if val1 != 0 else ip + 3
        elif opcode == 6: ip = val2 if val1 == 0 else ip + 3
        elif opcode == 7: instructions[instructions[ip + 3]]  = 1 if val1 < val2 else 0
        elif opcode == 8: instructions[instructions[ip + 3]] = 1 if val1 == val2 else 0
        if opcode in [1,2,7,8]: ip += 4
        if opcode in [3,4]: ip += 2
        opcode = instructions[ip] % 100
print("answer a: {}".format(solve(1)))
print("answer b: {}".format(solve(5)))