input = [0,1,5,10,3,12,19]
prev, seen = -1, {k:v+1 for v, k in enumerate(input)}

for i in range(len(input), 30000000):
  if prev in seen: speak = i - seen[prev]
  else: speak = 0
  seen[prev] = i
  prev = speak
  if i + 1 == 2020: print("Answer A:", speak)
print("Answer B:", speak)