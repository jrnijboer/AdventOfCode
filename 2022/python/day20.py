from collections import deque
inputnumbers = list(map(int, [line.strip() for line in open("../input/day20.input", encoding="utf-8").readlines()]))

def solve(numbers, multiplier, iterations):
    numbers = [n * multiplier for n in numbers]
    positionlist = deque([(n, i) for i, n in enumerate(numbers)])
    for _ in range(iterations):
        for i, n in enumerate(numbers):
            ix = positionlist.index((n, i))
            positionlist.rotate(-ix)
            item = positionlist.popleft()
            positionlist.rotate(-item[0])
            positionlist.append(item)
    mixed_numbers = [n for n, _ in positionlist]
    ix_zero = mixed_numbers.index(0)
    return (mixed_numbers[(ix_zero + 1000) % len(mixed_numbers)] + mixed_numbers[(ix_zero + 2000) % len(mixed_numbers)] + mixed_numbers[(ix_zero + 3000) % len(mixed_numbers)])

print("Answer A:", solve(inputnumbers, 1, 1))
print("Answer B:", solve(inputnumbers, 811589153, 10))
