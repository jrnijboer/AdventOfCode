def solve(part_b):
    def canmove(x, y, dx, dy):
        checks = [("[", 1), ("]", -1)]
        return any([grid[y][x] == bracket and (grid[y + dy][x + dx] == "." or canmove(x + dx, y + dy, dx, dy)) and (grid[y + dy][x + dx + i] == "." or canmove(x + dx+i, y + dy, dx, dy)) for (bracket, i) in checks])

    def movebox(x, y, dx, dy):
        if part_b:
            if dy == 0: # left/right
                if grid[y + 2*dy][x + 2*dx] == "." or (grid[y + 2*dy][x + 2*dx] in "[]" and movebox(x + 2*dx, y + 2*dy, dx, dy)):
                    grid[y + 2*dy][x + 2*dx] = grid[y+dy][x+dx]
                    grid[y + dy][x + dx] = grid[y][x]
                    grid[y][x] = "."
                    return True
            else: # up/down
                if grid[y][x] in "[]":
                    offset = 1 if grid[y][x] == "[" else -1
                    if (grid[y + dy][x + dx] == "." or canmove(x + dx, y + dy, dx, dy)) and (grid[y + dy][x + dx + offset] == "." or canmove(x + dx + offset, y + dy, dx, dy)):
                        for i, bracket in enumerate(["[", "]"] if offset == 1 else ["]", "["]):
                            movebox(x + dx + i * offset, y + dy, dx, dy)
                            grid[y + dy][x + dx + i * offset] = bracket
                            grid[y][x + i * offset] = "."
                        return True
        else:
            if grid[y + dy][x + dx] == "." or (grid[y + dy][x + dx] == "O" and movebox(x + dx, y + dy, dx, dy)):
                grid[y + dy][x + dx] = "O"
                grid[y][x] = "."
                return True
        return False

    grid, moves = open("../input/15.txt", encoding="utf-8").read().split("\n\n")
    movements = {"<": (-1, 0), ">": (1, 0), "^": (0, -1), "v": (0, 1)}

    if part_b:
        stretched_grid, robot = [], (0, 0)
        for y, row in enumerate(grid.split("\n")):
            gridrow = []
            for x, c in enumerate(row):
                if c == "#":
                    gridrow.extend(["#","#"])
                if c == ".":
                    gridrow.extend([".","."])
                if c == "@":
                    gridrow.extend(["@","."])
                    robot = (x*2, y)
                if c == "O":
                    gridrow.extend(["[","]"])
            stretched_grid.append(gridrow)
        grid = stretched_grid
    else:
        grid = [list(line) for line in grid.split("\n")]
        robot = next((x, y) for y, row in enumerate(grid) for x, char in enumerate(row) if char == "@")

    for move in moves.replace("\n", ""):
        dx, dy = movements[move]
        if grid[robot[1] + dy][robot[0] + dx] == ".":
            grid[robot[1]][robot[0]] = "."
            grid[robot[1] + dy][robot[0] + dx] = "@"
            robot = (robot[0] + dx, robot[1] + dy)

        elif grid[robot[1] + dy][robot[0] + dx] in "[]O":
            if movebox(robot[0] + dx, robot[1] + dy, dx, dy):
                grid[robot[1]][robot[0]] = "."
                grid[robot[1] + dy][robot[0] + dx] = "@"
                robot = (robot[0] + dx, robot[1] + dy)

    return sum(100 * y + x for y, row in enumerate(grid) for x, c in enumerate(row) if c in "[O")

print("Answer A:", solve(False))
print("Answer B:", solve(True))
