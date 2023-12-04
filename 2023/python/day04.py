lines = [line.strip().replace("  ", " ") for line in open("../input/day04.txt", encoding="utf-8").readlines()]
cards, scoreA = [1]* len(lines), 0

for cardnumber, line in enumerate(lines):
    winning, candidates = [part.split(" ") for part in line.split(" | ")]
    winning = [x for x in [int(x) for x in winning[2:] if x != ""]]
    winners = len([int(w) for w in winning if w in set([int(x) for x in candidates if x != ""])])
    if winners > 0:
        scoreA += 2**(winners - 1)
        for i in range(cardnumber + 1, cardnumber + 1 + winners):
            cards[i] += cards[cardnumber]

print(f"Answer A: {scoreA}")
print(f"Answer B: {sum(cards)}")
