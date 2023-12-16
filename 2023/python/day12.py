lines = [line.strip().split(" ") for line in open("../input/day12.txt", encoding="utf-8").readlines()]
answerA, answerB = 0, 0
seen = {}

def arrange(line, numbers):
    if len(line) == 0:
        return 0 if numbers else 1
    if not numbers:
        return 0 if "#" in line else 1

    key = (line, numbers)
    if key in seen:
        return seen[key]

    result = 0
    if line[0] == "?":
        result += arrange("." + line[1:], numbers) + arrange("#" + line[1:], numbers)
    elif line[0] == ".":
        result += arrange(line[1:], numbers)
    else:
        if len(line) >= numbers[0] and "." not in line[:numbers[0]] and (len(line) == numbers[0] or line[numbers[0]] != "#"):
            nextline = "." + line[numbers[0] + 1:]
            result += arrange(nextline, numbers[1:])
    seen[key] = result
    return result

for p1, p2 in lines:
    p2 = tuple(map(int, p2.split(",")))
    answerA += arrange(p1, p2)
    answerB += arrange("?".join([p1]*5), p2*5)

print(f"Answer A: {answerA}")
print(f"Answer B: {answerB}")
