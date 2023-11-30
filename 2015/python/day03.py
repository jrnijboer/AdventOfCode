from collections import defaultdict

directions = open("../input/day03.input").read()
x, y, xsanta, ysanta, xrobo, yrobo = 0, 0, 0, 0, 0, 0
H, Hb = defaultdict(int), defaultdict(int)

for i, d in enumerate(directions):
    if d == '>':
        x += 1
        if i % 2== 0:
            xsanta += 1
        else:
            xrobo += 1
    elif d == '<':
        x -= 1
        if i % 2== 0:
            xsanta -= 1
        else:
            xrobo -= 1
    elif d == '^':
        y += 1
        if i % 2== 0:
            ysanta += 1
        else:
            yrobo += 1
    elif d == 'v':
        y -= 1
        if i % 2== 0:
            ysanta -= 1
        else:
            yrobo -= 1
    H[(x,y)] += 1
    Hb[(xrobo,yrobo)] += 1
    Hb[(xsanta,ysanta)] += 1

print(f"Answer A: {len(H) + 1}")
print(f"Answer B: {len(Hb)}")
