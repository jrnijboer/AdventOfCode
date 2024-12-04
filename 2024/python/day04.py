lines = [line.strip() for line in open("../input/04.txt", encoding="utf-8").readlines()]
A, B = 0, 0

for y in range (len(lines)):
    for x in range(len(lines[0])):
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
            if 0 <= x + dx * 3 < len(lines[0]) and 0 <= y + dy * 3 < len(lines):
                if lines[y][x] + lines[y + dy ][x + dx] + lines[y + dy * 2][x + dx * 2] + lines[y + dy * 3][x + dx * 3] == "XMAS":
                    A += 1
        if 0 <= x - 1 < len(lines[0]) and 0 <= y + 1 < len(lines) and 0 <= x + 1 < len(lines[0]) and 0 <= y - 1 < len(lines):
            if lines[y + 1][x - 1] + lines[y][x] + lines[y - 1][x + 1] in ["MAS", "SAM"] and \
            lines[y + 1][x + 1] + lines[y][x] + lines[y - 1][x - 1] in ["MAS", "SAM"]:
                B += 1

print("Answer A:", A)
print("Answer B:", B)
