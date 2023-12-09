numberlines = [list(map(int, line.strip().split())) for line in open("../input/day09.txt", encoding="utf-8").readlines()]

def extrapolate(numbers):
    if all(i == 0 for i in numbers):
        return 0, 0
    first, last = extrapolate([y - x for x, y in zip(numbers, numbers[1:])])
    return numbers[0] - first, numbers[-1] + last

answers = [extrapolate(numbers) for numbers in numberlines]
print(f"Answer A: {sum([a for a, _ in answers])}")
print(f"Answer B: {sum([b for _, b in answers])}")
