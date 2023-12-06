from math import ceil, floor, prod
times, records = [line.split()[1:] for line in open("../input/day06.txt", encoding="utf-8")]
times = [int(x) for x in times if x != ""]
records = [int(x) for x in records if x != ""]

def score(time, dist):
    discriminant = time**2 - 4 * dist
    first = floor((time - discriminant**0.5) / 2)
    last = ceil((time + discriminant**0.5) / 2)
    return last - first - 1

print(f"Answer A: {prod(map(score, times, records))}")
print(f'Answer B: {score(int("".join(map(str, times))), int("".join(map(str, records))))}')
