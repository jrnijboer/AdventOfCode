lines = [line.strip().split(": ") for line in open("../input/07.txt", encoding="utf-8").readlines()]
A, B = 0, 0

def get_calibrations(digits, ops):
    calibrations = [digits[0]]
    for digit in digits[1:]:
        calibrations = [op(c, digit) for c in calibrations for op in ops]
    return calibrations

for result, values in lines:
    result = int(result)
    values = list(map(int, values.split()))
    if result in get_calibrations(values, [lambda l, r: l + r, lambda l, r: l * r]):
        A += result
    if result in get_calibrations(values, [lambda l, r: l + r, lambda l, r: l * r, lambda l, r: int(str(l) + str(r))]):
        B += result

print("Answer A:", A)
print("Answer B:", B)
