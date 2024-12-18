from heapq import heappush, heappop

grid = [list(line) for line in open("../input/16.txt", encoding="utf-8").read().split("\n")]
current_dir, S, E, visited = 1, (0, 0), (0, 0), set()
S = [(x, y) for y, line in enumerate(grid) for x, char in enumerate(line) if char == "S"][0]

def traverse(Q):
    a, b, cost = float("inf"), set(), 0
    while cost <= a:
        cost, x, y, cur_dir, path = heappop(Q)
        visited.add((x, y, cur_dir))
        if grid[y][x] == "E":
            a = min(a, cost)
            b.update(path)
            continue
        for d in [-1, 0, 1]:
            dx, dy = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}[(cur_dir + d) % 4]
            new_dir = (cur_dir + d) % 4
            next_cost = cost + 1 if d == 0 else cost + 1000
            if grid[y + dy][x + dx] != "#":
                if d == 0 and (x + dx, y + dy, new_dir) not in visited:
                    heappush(Q, (next_cost, x + dx, y + dy, new_dir, path + [(x + dx, y + dy)]))
            if d != 0 and (x , y , new_dir) not in visited:
                heappush(Q, (next_cost, x, y, new_dir, list(path)))
    return a, len(b)

A, B = traverse([(0, *S, current_dir, [S])])
print("Answer A:", A)
print("Answer B:", B)
