for noun in range(100):
    for verb in range(100):
        input = list(map(int,open("../input/day2.input").readline().split(",")))
        ip, opcode, input[1], input[2] = 0, input[0], noun, verb
        while opcode != 99:
            if opcode == 1: input[input[ip + 3]] = input[input[ip + 1]] + input[input[ip + 2]]
            if opcode == 2: input[input[ip + 3]] = input[input[ip + 1]] * input[input[ip + 2]]
            ip = ip + 4
            opcode = input[ip]
        if (noun == 12 and verb == 2): print ("answer a: {}".format(input[0]))
        if input[0] == 19690720: print ("answer b: {}".format(100 * noun + verb))
