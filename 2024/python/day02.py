lines = [list(map(int, line.strip().split())) for line in open("../input/02.txt", encoding="utf-8").readlines()]

def is_safe(levels):
    deltas = [y - x for x, y in zip(levels, levels[1:])]
    return all(1 <= delta <= 3 for delta in deltas) or all(-3 <= delta <= -1 for delta in deltas)

print("Answer A:", sum([1 if is_safe(line) else 0 for line in lines]))
print("Answer B:", sum({tuple(line): 1 for line in lines for i in range(len(line)) if is_safe(line[:i] + line[i+1:])}.values()))
