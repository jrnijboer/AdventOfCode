input, b = [line for line in open("../input/day06.input").read().split("\n\n") if line ], 0
print("Answer A:", len([c for c in "abcdefghijklmnopqrstuvwxyz" for line in input if c in line]))
for line in input:
  answers = set("abcdefghijklmnopqrstuvwxyz")
  for group in line.split(): answers = answers.intersection(group)
  b += len(answers)
print("Answer B:", b)
