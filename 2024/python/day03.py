import re
memory = open("../input/03.txt").read()
pattern = r"mul\(\d+,\d+\)"
print("Answer A:", sum(l * r for l, r in (map(int, re.findall(r"\d{1,3}", match)) for match in re.findall(pattern, memory))))

B = 0
for enabledmemory in re.findall(r"do\(\).*?don't\(\)", "do()" +  memory + "don't()", re.DOTALL):
    B += sum(l * r for l, r in (map(int, re.findall(r"\d{1,3}", match)) for match in re.findall(pattern, enabledmemory)))
print("Answer B:", B)
