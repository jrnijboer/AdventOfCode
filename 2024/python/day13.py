import re
games = open("../input/13.txt", encoding="utf-8").read().split("\n\n")
A, B = 0, 0

def solve_b(x1, y1, x2, y2, x, y):
    tmp_x2, tmp_x = x2, x
    x2, y2, x, y = y1 * x2, x1 * y2, y1 * x, x1 * y

    if (x - y) % (x2 - y2) != 0:
        return 0
    b = (x - y) // (x2 - y2)
    x = tmp_x - tmp_x2 * b
    if x % x1 != 0:
        return 0
    return (x // x1)*3 + b

for i, game in enumerate(games):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", game))
    A += solve_b(ax, ay, bx, by, px, py)
    B += solve_b(ax, ay, bx, by, px+10000000000000, py+10000000000000)

print("Answer A:", A)
print("Answer B:", B)
