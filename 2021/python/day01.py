input = [int(i.strip()) for i in open("../input/day01.input").readlines()]
avg = [input[i] + input[i-1] + input[i-2] for i in range(2, len(input))]
print ("Answer A:", sum([a < b for a, b in zip(input, input[1:])]))
print ("Answer B:", sum([a < b for a, b in zip(avg, avg[1:])]))
