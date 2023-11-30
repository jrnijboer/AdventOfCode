braces = open("../input/day01.input").read().strip()
floor, b = 0, 0
for i, c in enumerate(braces):
    if c == '(':
        floor += 1
    elif c == ')':
        floor -=1
    if b == 0 and floor < 0:
        b = i + 1
print(f'Answer A: {floor}')
print(f'Answer B: {b}')
