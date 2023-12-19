workflowinput, partsinput =  open("../input/day19.txt", encoding="utf-8").read().strip().split("\n\n")
A, B, W = 0, 0, {}

def process(parts, workflow):
    if workflow in "AR":
        return workflow

    rules, dest = W[workflow]
    for rule in rules:
        cmpr, ruledest = rule.split(":")
        category = cmpr[0]
        operator = cmpr[1]
        val = int(cmpr[2:])
        if operator == "<":
            if parts[category] < val:
                return process(parts, ruledest)
        elif parts[category] > val:
            return process(parts, ruledest)
    return process(parts, dest)

for line in workflowinput.split("\n"):
    name, rules = line.split("{")
    rules, dest = rules[:-1].rsplit(",", 1)
    W[name] = (rules.split(","), dest)

for line in partsinput.split("\n"):
    parts = line[1:-1].split(",")
    parts = {part.split("=")[0]: int(part.split("=")[1]) for part in parts}
    if (process(parts, "in")) == "A":
        A += sum(parts.values())
print("Answer A:", A)

Q = [("in", { "x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000) })]
while Q:
    workflow, ranges = Q.pop()
    if workflow == "A":
        prod = 1
        for v in ranges.values():
            prod *= (1 + v[1] - v[0])
        B += prod
        continue
    if workflow == "R":
        continue

    rules, dest = W[workflow]
    for rule in rules:
        cmpr, ruledest = rule.split(":")
        category = cmpr[0]
        operator = cmpr[1]
        val = int(cmpr[2:])
        if ranges[category][0] < val < ranges[category][1]:
            redirect = {k: v for (k, v) in ranges.items() if k != category }
            if operator == "<":
                redirect[category] = (ranges[category][0], val -1)
                ranges[category] = (val, ranges[category][1])
            else:
                redirect[category] = (val + 1, ranges[category][1])
                ranges[category] = (ranges[category][0], val)
            Q.append((ruledest, redirect))
    Q.append((dest, dict(ranges)))

print("Answer B:", B)
