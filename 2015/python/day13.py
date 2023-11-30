from itertools import permutations
from collections import defaultdict
happinesslines = [line.strip().split() for line in open("../input/day13.input", encoding="utf-8").readlines()]

def solve(partB = False):
    H = defaultdict(int, {h[0][0] + h[-1][0] : int(h[3]) * (-1 if h[2] == "lose" else 1) for h in happinesslines})
    players = ''.join(set(''.join(H.keys())))
    if partB:
        players += "Q"
    setups = list(permutations(players, len(players)))
    maxhappiness = 0
    for setup in setups:
        happiness = 0
        for i, player in enumerate(setup):
            happiness += H[player+setup[(i+1) % len(setup)]]
            happiness += H[setup[(i+1) % len(setup)] + player]
        maxhappiness = max(happiness, maxhappiness)
    return maxhappiness

print("Answer A:", solve())
print("Answer B:", solve(True))