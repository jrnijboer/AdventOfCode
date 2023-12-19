lines = open("../input/day18.txt", encoding="utf-8").read().splitlines()

def shoelace(partB=False):
    DIR = {"D": (1, 0), "L": (0, -1), "U": (-1, 0), "R": (0, 1)}
    row, col, bordersize, corners = 0, 0, 0, []

    # shoelace formula: https://www.theoremoftheday.org/GeometryAndTrigonometry/Shoelace/TotDShoelace.pdf
    # explainer: https://www.youtube.com/watch?v=bGWK76_e-LM
    for line in lines:
        if partB:
            _, _, color = line.split(" ")
            direction = "RDLU"[int(color[7])]
            distance = int(color[2:7], 16)
        else:
            direction, distance, _ = line.split(" ")
            distance = int(distance)

        dr, dc = DIR[direction]
        bordersize += distance
        row += distance * dr
        col += distance * dc
        corners.append((row, col))
    inside_area = sum([x0 * y1 - x1 * y0 for (x0, y0), (x1, y1) in zip(corners, corners[1:])])
    return abs(inside_area), bordersize

a, b = shoelace()
print("Answer A:", a//2 + b//2 + 1)
a, b = shoelace(True)
print("Answer B:", a//2 + b//2 + 1)
