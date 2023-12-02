from collections import defaultdict
gamelines = [line.strip() for line in open("../input/day02.txt", encoding="utf-8").readlines()]
A, B = 0, 0
for line in gamelines:
    game, rounds = line.split(": ")
    red, blue, green, valid, results = 0, 0, 0, True, defaultdict(int)
    for round in rounds.split(";"):
        for take in round.split(","):
            amount, colour = take.split()
            results[colour] = max(results[colour], int(amount))
            if int(amount) > {"red": 12, "green": 13, "blue": 14}.get(colour):
                valid = False
    if valid:
        A += int(game.split()[1])
    B += results["red"] * results["blue"] * results["green"]

print(f"Answer A: {A}")
print(f"Answer B: {B}")
