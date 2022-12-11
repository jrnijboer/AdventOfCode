def solve(n, divisor):
    monkeys = open("../input/day11.input", encoding="utf-8").read().split("\n\n")
    prodPrimes, inv, test, oper, action, insp = 1, {}, {}, {}, {}, {}
    for ix, parts in enumerate([line.splitlines() for line in monkeys]):
        insp[ix] = 0
        inv[ix] = [int(item) for item in parts[1].split(":")[1].split(",")]
        new = parts[2].split("new = ")[1].split(" ")
        if new[1] == "+":
            oper[ix] = lambda old, new = new: old + (int(new[2]) if new[2].isnumeric() else old)
        elif new[1] == "*":
            oper[ix] = lambda old, new = new: old * (int(new[2]) if new[2].isnumeric() else old)
        test[ix] = int(parts[3].split(": ")[1].split()[2])
        prodPrimes *= int(parts[3].split(": ")[1].split()[2])
        action[ix] = {True: int(parts[4].split()[5]), False: int(parts[5].split()[5])}
    for _ in range(n):
        for monkey, inventory in inv.items():
            for item in inventory:
                insp[monkey] += 1
                item = (oper[monkey](item) % prodPrimes) // divisor
                inv[action[monkey][item % test[monkey] == 0]].append(item)
            inv[monkey] = []
    insp = (sorted(insp.values(), reverse=True))
    return insp[0] * insp[1]

print("Answer A:", solve(20, 3))
print("Answer B:", solve(10000, 1))
