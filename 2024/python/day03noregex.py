memory = open("../input/03.txt").read()
A, B, mul = 0, 0, 1

for i in range(len(memory)):
    if memory[i : i + 4] == "mul(":
        parts = memory[i + 4 : memory.find(")", i + 4)].split(",")
        if len(parts) == 2 and all(part.isdigit() for part in parts):
            A += int(parts[0]) * int(parts[1])
            B += int(parts[0]) * int(parts[1]) * mul
    elif memory[i:].startswith("do()"):
        mul = 1
    elif memory[i:].startswith("don't()"):
        mul = 0

print("Answer A:", A)
print("Answer B:", B)
