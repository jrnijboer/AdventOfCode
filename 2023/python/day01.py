lines = [line.strip() for line in open("../input/day01.txt", encoding="utf-8").readlines()]
sumA, sumB = 0, 0
NumberDict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def replaceStringWithNumber(line):
    i, replacedLine = 0, ""
    while i < len(line):
        replacedLine += "".join([n for s, n in NumberDict.items() if line[i:].startswith(s)])
        replacedLine += line[i]
        i += 1
    return replacedLine

def getFirstNumber(line):
    return [i for i in line if i.isdigit()][0]

for line in lines:
    sumA += int(getFirstNumber(line) + getFirstNumber(line[::-1]))
    sumB += int(getFirstNumber(replaceStringWithNumber(line)) + getFirstNumber(replaceStringWithNumber(line)[::-1]))

print(f"Answer A: {sumA}")
print(f"Answer B: {sumB}")
