def getMostCommonBit(input:list, pos:int):
    ones = len([line for line in input if line[pos] == '1'])
    return 1 if ones >= len(input) - ones else 0

def toInt(binaryString:str):
    return int("".join([str(i) for i in binaryString]), 2)

input = [i.strip() for i in open("../input/day03.input").readlines()]

gamma = [getMostCommonBit(input, i) for i in range(len(input[0]))]
print("Answer A:", (2**(len(input[0])) -1 - toInt(gamma)) * toInt(gamma))


oxygen, co2 = input.copy(), input.copy()
for i in range(len(input[0])):
    if len(oxygen) > 1:
        commonOxygen = getMostCommonBit(oxygen, i)
        oxygen = [line for line in oxygen if line[i] == str(commonOxygen)]
    if len(co2) > 1:
        commonCo2 = getMostCommonBit(co2, i)
        co2 = [line for line in co2 if line[i] != str(commonCo2)]

print("Answer B:", toInt(oxygen) * toInt(co2))
