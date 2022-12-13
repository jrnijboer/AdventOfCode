from functools import cmp_to_key
listpairs = open("../input/day13.input", encoding="utf-8").read().split("\n\n")
A, B, L = 0, 1, [[[2]], [[6]]]

def compare(list1, list2):
    if isinstance(list1, int) and isinstance(list2, int):
        return list1 - list2
    if isinstance(list1, int) and isinstance(list2, list):
        return compare([list1], list2)
    if isinstance(list1, list) and isinstance(list2, int):
        return compare(list1, [list2])
    if isinstance(list1, list) and isinstance(list2, list):
        for combination in zip(list1, list2):
            res = compare(combination[0], combination[1])
            if res != 0:
                return res
        return len(list1) - len(list2)

for ix, pair in enumerate(listpairs):
    parts = pair.splitlines()
    l1, l2 = eval(parts[0]), eval(parts[1])
    L.append(l1)
    L.append(l2)
    if compare(l1, l2) < 0:
        A += ix + 1

L.sort(key=cmp_to_key(compare))
for ix, line in enumerate(L):
    if line in [[[6]], [[2]]]:
        B *= ix + 1

print("Answer A:", A)
print("Answer B:", B)
