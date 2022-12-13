from collections import deque
S, E, G = (), (), {}
for y, line in enumerate(open("../input/day12.input", encoding="utf-8").readlines()):
    for x, c in enumerate(line.strip()):
        if c == 'S':
            S = (x, y)
            G[x,y] = 1
        elif c == 'E':
            E = (x, y)
            G[x,y] = 26
        else:
            G[x,y] = ord(c) - 96

def solve(start, grid, is_done, move_valid):
    V, Q = set(), deque([(start, 0)])
    while Q:
        cur, dist = Q.popleft()
        if is_done(cur, E, grid):
            return dist
        V.add(cur)
        for dxy in [(0,-1),(0,1),(1,0),(-1,0)]:
            cand = (cur[0] + dxy[0], cur[1] + dxy[1])
            if cand in grid and cand not in V and move_valid(grid[cur], grid[cand]):
                Q.append((cand, dist + 1))
                V.add(cand)

print("Answer A:", solve(S, G, lambda pos, E, G: pos == E, lambda p1, p2: p1 >= p2 -1))
print("Answer B:", solve(E, G, lambda pos, E, G: G[pos] == 1, lambda p1, p2: p1 - 1 <= p2))
