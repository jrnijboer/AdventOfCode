rps = [line.strip() for line in open("../input/day02.input", encoding="utf-8").readlines()]
A = { "A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6 }
B = { "A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7 }
print(f"Answer A: {sum([A[game] for game in rps])}")
print(f"Answer B: {sum([B[game] for game in rps])}")
