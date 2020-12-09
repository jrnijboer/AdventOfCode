import itertools
numbers = [int(line.strip()) for line in open("../input/day09.input").readlines()]
preamble, offset = 25, 0

for number in numbers[preamble:]:
  if not any ([x + y == number for x, y in list(itertools.combinations(numbers[offset:offset + preamble], 2))]):
    print("Answer A:", number)
    break
  offset += 1

for i in range(len(numbers)):
  if numbers[i] == number: continue
  for j in range(i + 1, len(numbers)):
    if sum(numbers[i:j]) == number: print("Answer B:", min(numbers[i:j]) + max(numbers[i:j]))      
    if sum(numbers[i:j]) > number: break
