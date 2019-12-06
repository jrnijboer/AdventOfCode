def route(input, o):
    while o in input:
        yield input[o]
        o = input[o]
input = {k:v for (v,k) in [line.strip("\n").split(")") for line in open("../input/day6.input").readlines()]}
print("answer a: {}".format(sum([len(list(route(input, i))) for i in input])))
print("answer b: {}".format(len(set(route(input, 'SAN')) ^ set(route(input, 'YOU')))))