lines = [i.strip() for i in open("../input/day11.input", encoding="utf-8").readlines()]
steps, A, C, R = 0, 0, len(lines[0]), len(lines)
deltas = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
G = {(col, row): int(lines[row][col]) for col in range(C) for row in range(R)}

def do_increment(pos, hasflashed, S):
    G[pos] += 1
    if G[pos] > 9:
        S.add(pos)
        hasflashed.add(pos)
        G[pos] = 0
        return 1
    return 0

while True:
    steps += 1
    B, hasflashed, S = 0, set(), set()
    for k in G.keys():
        B += do_increment(k, hasflashed, S)

    while S:
        pos = S.pop()
        for d in deltas:
            c, r = pos[0] + d[0], pos[1] + d[1]
            if 0 <= c < C and 0 <= r < R and (c, r) not in hasflashed:
                B += do_increment((c, r), hasflashed, S)
    A += B

    if steps == 100:
        print("Answer A:", A)
    if B == C * R:
        print("Answer B", steps)
        break
