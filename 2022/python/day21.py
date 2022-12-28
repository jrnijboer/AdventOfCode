lines = [line.strip() for line in open("../input/day21.input", encoding="utf-8").readlines()]

def getValue(s):
    val = operations[s]
    if val.isnumeric():
        return int(val)
    else:
        l, oper, r = val.split(" ")
        if oper == "+":
            return getValue(l) + getValue(r)
        elif oper == "-":
            return getValue(l) - getValue(r)
        elif oper == "*":
            return getValue(l) * getValue(r)
        elif oper == "/":
            return getValue(l) / getValue(r)

operations = {}
for line in lines:
    var, val = line.split(":")
    operations[var] = val[1:]
print("Answer A:", int(getValue("root")))

target, x, delta, lo, hi = 0, 0, 0, 0, 1000000000000000
l, _, r = operations["root"].split(" ")
L1, R1 = getValue(l), getValue(r)
operations["humn"] = "0"
L2, R2 = getValue(l), getValue(r)
if (L1 != L2 and R1 == R2):
    target = R1
    x = l
    delta = L1 - L2
elif (L1 == L2 and R1 != R2):
    target = L1
    x = r
    delta = R1 - R2

while lo != hi:
    mid = (lo + hi) // 2
    operations["humn"] = str(mid)
    res = getValue(x)
    if res == target:
         print("Answer B:", mid)
         break
    elif res > target and delta < 0:
        lo = mid
    elif res < target and delta < 0:
        hi = mid
    elif res < target and delta > 0:
        lo = mid
    elif res > target and delta > 0:
        hi = mid
