import re
memory = open("../input/03.txt", encoding="utf-8").read()
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
print("Answer A:", sum(int(match[0]) * int(match[1]) for match in re.findall(pattern, memory)))

B = 0
for enabledmemory in re.findall(r"do\(\).*?don't\(\)", "do()" +  memory + "don't()", re.DOTALL):
    B += sum(int(match[0]) * int(match[1]) for match in re.findall(pattern, enabledmemory))
print("Answer B:", B)
