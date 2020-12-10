from collections import defaultdict
numbers = sorted([int(line.strip()) for line in open("../input/day10.input").readlines()])

j, d1, d3 = 0, 0, 1
for n in range(len(numbers)):  
  if numbers[n] - j == 1: d1 += 1
  elif numbers[n] - j == 3: d3 += 1
  j += numbers[n] - j
print("Answer A:", d1 * d3)

D = defaultdict(int, {1:1, 2:2, 3:4}) # works because lowest 3 values in input are 1,2,3
for n in numbers[3:]:  
  D[n] = D[n-1] + D[n-2] + D[n-3]
print("Answer B:", D[max(D.keys())])
