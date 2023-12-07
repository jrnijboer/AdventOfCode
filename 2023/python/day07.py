from collections import Counter
lines = [line.strip() for line in open("../input/day07.txt", encoding="utf-8").readlines()]

def PlayPoker(lines, replacement):
    hands = []
    for line in lines:
        hand, amount = line.split()
        cards = Counter(hand)
        jokers = cards["J"]
        if replacement == "0":
            if jokers > 0:
                del(cards["J"])
            if cards:
                cards = sorted(cards.values(), reverse=True)
                cards[0] += jokers
            else:
                cards = [5]
        else:
            cards = sorted(cards.values(), reverse=True)
        ranks = {(5,): 6, (4,1): 5, (3,2): 4, (3,1,1): 3, (2,2,1): 2, (2,1,1,1): 1, (1,1,1,1,1): 0}
        strength = ranks[tuple(cards)]
        hands.append((strength, int(amount), hand.replace("A", "E").replace("K", "D").replace("Q", "C").replace("J", replacement).replace("T", "A")))
    hands.sort(key=lambda x: str(x[0]) + x[2])
    return sum([(i +1) * hand[1] for i, hand in enumerate(hands)])

print(f'Answer A: {PlayPoker(lines, "B")}')
print(f'Answer A: {PlayPoker(lines, "0")}')
