def route(input, o):
    steps = []
    while o in input:
        steps.append(input[o])
        o = input[o]
    return set(steps)
input = {k:v for (v,k) in [line.strip("\n").split(")") for line in open("../input/day6.input").readlines()]}
print("answer a: {}".format(sum([len(route(input, i)) for i in input])))
print("answer b: {}".format((len(route(input, 'SAN') ^ route(input, 'YOU')))))