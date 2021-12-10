def get_most_common_bit(bitlines: list, pos: int):
    ones = len([line for line in bitlines if line[pos] == '1'])
    return 1 if ones >= len(bitlines) - ones else 0

def to_int(binary_string: str):
    return int("".join([str(i) for i in binary_string]), 2)

lines = [i.strip() for i in open("../input/day03.input", encoding="utf-8").readlines()]
gamma = [get_most_common_bit(lines, i) for i in range(len(lines[0]))]
print("Answer A:", (2**(len(lines[0])) - 1 - to_int(gamma)) * to_int(gamma))

oxygen, co2 = lines.copy(), lines.copy()
for i in range(len(lines[0])):
    if len(oxygen) > 1:
        common_oxygen = get_most_common_bit(oxygen, i)
        oxygen = [line for line in oxygen if line[i] == str(common_oxygen)]
    if len(co2) > 1:
        common_co2 = get_most_common_bit(co2, i)
        co2 = [line for line in co2 if line[i] != str(common_co2)]
print("Answer B:", to_int(oxygen) * to_int(co2))
