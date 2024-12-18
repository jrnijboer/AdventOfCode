G = [list(line.strip()) for line in open("../input/12.txt", encoding="utf-8")]
flooded_tiles, flooded_areas = set(), []
A, B = 0, 0

def flood(x, y, c, area):
    if 0 <= x < len(G[0]) and 0 <= y < len(G) and G[y][x] == c:
        area.add((x, y))
        flooded_tiles.add((x, y))
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (x + dx, y + dy) not in flooded_tiles:
                flood(x + dx, y + dy, c, area)
    return area

def count_corners(x, y, area):
    corner_count = 0
    # outside corners
    if (x + 1, y) not in area and (x, y + 1) not in area:
        corner_count += 1
    if (x - 1, y) not in area and (x, y + 1) not in area:
        corner_count += 1
    if (x + 1, y) not in area and (x, y - 1) not in area:
        corner_count += 1
    if (x - 1, y) not in area and (x, y - 1) not in area:
        corner_count += 1

    # inside corners
    if (x + 1, y + 1 ) not in area and (x + 1, y) in area and (x, y + 1) in area:
        corner_count += 1
    if (x - 1, y + 1 ) not in area and (x - 1, y) in area and (x, y + 1) in area:
        corner_count += 1
    if (x + 1, y - 1 ) not in area and (x + 1, y) in area and (x, y - 1) in area :
        corner_count += 1
    if (x - 1, y - 1 ) not in area and (x - 1, y) in area and (x, y - 1) in area:
        corner_count += 1
    return corner_count

for Y, row in enumerate(G):
    for X, char in enumerate(row):
        if (X, Y) not in flooded_tiles:
            flooded_areas.append((flood(X, Y, char, set()), char))

for flooded_area, char in flooded_areas:
    perimeter = 0
    corners = 0
    for X, Y in flooded_area:
        perimeter += 4 - sum([1 if (X + dx, Y + dy) in flooded_area else 0 for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]])
        corners += count_corners(X, Y, flooded_area)
    A += perimeter * len(flooded_area)
    B += corners * len(flooded_area)

print("Answer A:", A)
print("Answer B:", B)
