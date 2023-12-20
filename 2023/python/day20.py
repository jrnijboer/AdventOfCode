import math
def push(n, partB=False):
    lines =  open("../input/day20.txt", encoding="utf-8").read().strip().splitlines()
    modules, F, C, B, cycles = {}, {}, {}, [], {}
    for line in lines:
        l, r = line.split(" -> ")
        modules[l[0 if l.startswith("broadcaster") else 1:]] = r.split(", ")
        if r == "rx":
            rxsender = l[1:]
        if l.startswith("%"):
            F[l[1:]] = False
        elif l.startswith("&"):
            C[l[1:]] = dict()

    for module, targets in modules.items():
        for target in targets:
            if target in C.keys():
                C[target][module] = False
            if target == rxsender:
                cycles[module] = 0

    low, high, i = 0, 0, 0
    while i < n or partB:
        i += 1
        low += 1
        Q = [(module, False, "broadcaster") for module in modules["broadcaster"]]
        while Q:
            module, signal, sender = Q.pop(0)
            high += 1 if signal else 0
            low += 0 if signal else 1
            if module in F and not signal:
                F[module] = not F[module]
                for target in modules[module]:
                    Q.append((target, F[module], module))
            elif module in C:
                if module == rxsender and signal and sender in cycles.keys():
                    cycles[sender] = i
                    if all([val > 0 for val in cycles.values()]):
                        return math.lcm(*cycles.values())
                C[module][sender] = signal
                for target in modules[module]:
                    Q.append((target, not all([val for val in C[module].values()]), module))
    return low * high

print("Answer A:", push(1000))
print("Answer B:", push(0, True))
