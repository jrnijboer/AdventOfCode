import sys
inputs, connections = open("../input/24.txt", encoding="utf-8").read().split("\n\n")
I = {}
for inp in inputs.split("\n"):
    k, v = inp.split(": ")
    I[k] = int(v)

connections = connections.strip().split("\n")

while connections:
    next_connections = []
    for conn in connections:
        l, dest = conn.split(" -> ")
        a, oper, b = l.split(" ")
        if a in I and b in I:
            if oper == "AND":
                I[dest] = I[a] & I[b]
            elif oper == "OR":
                I[dest] = I[a] | I[b]
            elif oper == "XOR":
                I[dest] = I[a] ^ I[b]
        else:
            next_connections.append(conn)
    connections = next_connections

res = ""
for k in sorted(I):
    if k.startswith("z"):
        res = str(I[k]) + res

print("Answer A:", int(res, 2))

# part B:

# Observed rules:
# * Z nodes have two XOR parents
# * Z nodes have two XOR steps to the Y node and two XOR steps to the X node
# * X and Y nodes have one AND child and one XOR child
# * The parents of OR nodes have two AND parents

# after visual inspection, we can see that the following swaps are needed:
# swaps =[
#  ("z10", "mkk"),
#  ("z14", "qbw"),
#  ("z34", "wcb"),
#  ("wjb", "cvp")
# ]
