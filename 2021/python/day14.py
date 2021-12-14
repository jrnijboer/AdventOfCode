from collections import Counter, defaultdict
polymer, rulelines = open("../input/day14.input", encoding="utf-8").read().split("\n\n")
rules = {p1: p2 for p1, p2 in [rule.split(" -> ") for rule in rulelines.split("\n")]}

def solve(polymer: str, iterations: int):
    pairs = Counter([left + right for left, right in zip(polymer, polymer[1:])])

    for _ in range(iterations):
        Pnew = defaultdict(int)
        for k, v in pairs.items():
            Pnew[k[0] + rules[k]] += v
            Pnew[rules[k] + k[1]] += v
        pairs = Pnew

    totals = defaultdict(int)
    for k, v in pairs.items():
        totals[k[0]] += v
    totals[polymer[-1]] += 1

    return max(totals.values()) - min(totals.values())

print("Answer A:", solve(polymer, 10))
print("Answer B:", solve(polymer, 40))
