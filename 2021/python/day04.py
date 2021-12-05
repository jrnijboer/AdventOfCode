def make_bingo_card(lines: list):
    card = [[int(i) for i in row.split()] for row in lines]
    for i in range(5):
        card.append([card[0][i], card[1][i], card[2][i], card[3][i], card[4][i]])
    return card

def play_bingo_round(cards: dict, calledNumber: int):
    bingoCards = set()
    for cardId, card in cards.items():
        for row in card:
            if calledNumber in row:
                row.remove(calledNumber)
                if len(row) == 0:
                    bingoCards.add(cardId)
    return bingoCards

text = open("../input/day04.input", encoding="utf-8").read()
parts = text.split("\n\n")
rng = [int(i) for i in parts[0].split(",")]
remainingCards = {i: make_bingo_card(arr.split("\n")) for i, arr in enumerate(parts[1:])}

firstBingoFound = False
for number in rng:
    for fullCard in play_bingo_round(remainingCards, number):
        remainingNrsOnCard = {i for row in remainingCards[fullCard] for i in row}
        if not firstBingoFound:
            firstBingoFound = True
            print("Answer A:", sum(remainingNrsOnCard) * number)
        del remainingCards[fullCard]
        if not remainingCards:
            print("Answer B:", sum(remainingNrsOnCard) * number)
