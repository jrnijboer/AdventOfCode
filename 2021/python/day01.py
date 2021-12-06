numbers = [int(i.strip()) for i in open("../input/day01.input", encoding="utf-8").readlines()]
avg = [numbers[i] + numbers[i-1] + numbers[i-2] for i in range(2, len(numbers))]
print("Answer A:", sum([a < b for a, b in zip(numbers, numbers[1:])]))
print("Answer B:", sum([a < b for a, b in zip(avg, avg[1:])]))
