input = [line.strip() for line in open("../input/day08.input").readlines()]

def solve(input):
  acc, pointer, visited = 0, 0, set()
  while pointer not in visited and pointer < len(input):
    visited.add(pointer)
    operator, argument = input[pointer].split(" ")
    if operator == "acc": acc += int(argument)
    pointer += int(argument) if operator == "jmp" else 1
  return acc, pointer

def patch(input, i):
  patched = input.copy()
  operator, argument = patched[i].split(" ")
  patched[i] = "nop " + argument if operator == "jmp" else "jmp " + argument
  return patched

print("Answer A:", solve(input)[0])
print("Answer B:", [b for b, ip in [solve(patch(input, i)) for i in range(len(input)) if not input[i].startswith("acc")] if ip >= len(input)][0])
