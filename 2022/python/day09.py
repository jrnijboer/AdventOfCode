steps = [line.strip() for line in open("../input/day09.input", encoding="utf-8").readlines()]
A, B, R = {(0,0)}, {(0,0)}, [(0,0)]*10
D = {"U": [0, -1], "D": [0, 1], "L": [-1, 0], "R": [1, 0]}

for parts in [step.split() for step in steps]:
    for _ in range(int(parts[1])):
        R[0] = (R[0][0] + D[parts[0]][0], R[0][1] + D[parts[0]][1])
        for i in range(1, len(R)):
            dx = R[i - 1][0] - R[i][0]
            dy = R[i - 1][1] - R[i][1]
            if dx == 0 and abs(dy) > 1:
                R[i] = (R[i][0], R[i][1] + (1 if dy > 0 else -1))
            elif abs(dx) > 1 and dy == 0:
                R[i] = (R[i][0] + (1 if dx > 0 else -1), R[i][1])
            elif dx <= -1 and dy == -2 or dx == -2 and dy <= -1 : #R[i] goes up-left
                R[i] = (R[i][0] - 1, R[i][1] - 1)
            elif dx >= 1 and dy == -2 or dx == 2 and dy <= -1: #R[i] goes upright
                R[i] = (R[i][0] + 1, R[i][1] - 1)
            elif dx <= -1 and dy == 2 or dx == -2 and dy >= 1: #R[i] goes down-left
                R[i] = (R[i][0] - 1, R[i][1] + 1)
            elif dx >= 1 and dy == 2 or dx == 2 and dy >= 1: #R[i] goes down-right
                R[i] = (R[i][0] + 1, R[i][1] + 1)
            A.add(R[1])
            B.add(R[9])

print("Answer A:", len(A))
print("Answer B:", len(B))
