codes = open("../input/21.txt", encoding="utf-8").read().strip().split("\n")

num_grid = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["#", "0", "A"]
]

dir_grid = [
    ["#", "^", "A"],
    ["<", "v", ">"]
]

def get_route(start, end, keypad):
    # Button priority: Left, Up, Down, Right
    ax, ay = start
    bx, by = end
    dx = 1 if ax < bx else -1 if ax > bx else 0
    dy = 1 if ay < by else -1 if ay > by else 0
    hor = ">" if dx > 0 else "<" if dx < 0 else "H"
    vert = "v" if dy > 0 else "^" if dy < 0 else "V"
    path = ""
    # NW = Left and Up
    if dx < 0 and dy < 0:
        valid = True
        while ax != bx:
            ax += dx
            if keypad[ay][ax] == "#":
                valid = False
            path += hor
        while ay != by:
            ay += dy
            if keypad[ay][ax] == "#":
                valid = False
            path += vert
        if not valid:
            path = str(path[::-1])
    # NE = Up and Right
    elif dx > 0 and dy < 0:
        valid = True
        while ay != by:
            ay += dy
            if keypad[ay][ax] == "#":
                valid = False
            path += vert
        while ax != bx:
            ax += dx
            if keypad[ay][ax] == "#":
                valid = False
            path += hor
        if not valid:
            path = str(path[::-1])
    # N =  Up
    # S = Down
    elif dx == 0 and dy != 0:
        while ay != by:
            ay += dy
            path += vert
    # E =  Right
    # W =  Left
    elif dx != 0 and dy == 0:
        while ax != bx:
            ax += dx
            path += hor
    # SE = Down and Right
    elif dx > 0 and dy > 0:
        valid = True
        while ay != by:
            ay += dy
            if keypad[ay][ax] == "#":
                valid = False
            path += vert
        while ax != bx:
            ax += dx
            if keypad[ay][ax] == "#":
                valid = False
            path += hor
        if not valid:
            path = str(path[::-1])
    # SW = Left and Down
    elif dx < 0 and dy > 0:
        valid = True
        while ax != bx:
            ax += dx
            if keypad[ay][ax] == "#":
                valid = False
            path += hor
        while ay != by:
            ay += dy
            if keypad[ay][ax] == "#":
                valid = False
            path += vert
        if not valid:
            path = str(path[::-1])
    return path + "A"

def get_paths(keypad):
    buttons = {}
    for y, line in enumerate(keypad):
        for x, char in enumerate(line):
            if char != "#":
                buttons[char] = (x, y)

    paths = {}
    for a, start in buttons.items():
        for b, end in buttons.items():
            if a == b:
                paths[(a, b)] = "A"
            else:
                paths[(a, b)] = get_route(start, end, keypad)
    return(paths)

A, B = 0, 0
num_paths = get_paths(num_grid)
dir_paths = get_paths(dir_grid)

seen = {}
def get_directions_length(route, depth):
    if (route, depth) in seen:
        return seen[(route, depth)]
    if depth == 0:
        return len(route)
    length = 0
    for a, b in zip("A" + route, route):
        res = get_directions_length(dir_paths[(a, b)], depth -1)
        seen[(dir_paths[(a, b)], depth -1)] = res
        length += res
    return length

for code in codes:
    route = ""
    for a, b in zip("A" + code, code):
        route += num_paths[(a, b)]
    a = get_directions_length(route, 2)
    b = get_directions_length(route, 25)
    nr = int(code[:3])
    A += nr * a
    B += nr * b

print("Answer A:", A)
print("Answer B:", B)
