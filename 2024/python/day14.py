import re
bots = [(x, y, dx, dy) for line in open("../input/14.txt", encoding="utf-8") for x, y, dx, dy in [map(int, re.findall(r"-?\d+", line))]]
botpositions = {i:(x,y) for i, (x, y, _, _) in enumerate(bots)}
botvelocities = {i:(dx,dy) for i, (_, _, dx, dy) in enumerate(bots)}
width, height, seconds = 101, 103, 0
q1, q2, q3, q4 = 0, 0, 0, 0
grid = {(x, y): 0 for y in range(height) for x in range(width)}

for _ in range(100):
    for i, (x, y, dx, dy) in enumerate(bots):
        bots[i] = ((x + dx)%width, (y + dy)%height, dx, dy)

for x, y, _, _ in bots:
    grid[(x, y)] += 1
    q1 += x < width//2 and y < height//2
    q2 += x < width//2 and y > height//2
    q3 += x > width//2 and y < height//2
    q4 += x > width//2 and y > height//2

while True:
    seconds += 1
    for i, (x, y) in botpositions.items():
        dx,dy = botvelocities[i]
        botpositions[i] = ((x + dx)%width, (y + dy) % height)
    if len(set(botpositions.values())) == len(botpositions):
        print("\n".join("".join("#" if (x, y) in botpositions.values() else " " for x in range(width)) for y in range(height)))
        break

print("Answer A:", q1*q2*q3*q4)
print("Answer B:", seconds)
