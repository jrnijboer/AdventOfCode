from collections import defaultdict
patterns, designs = open("../input/19.txt", encoding="utf-8").read().split("\n\n")
patterns = patterns.strip().split(", ")
designs = designs.strip().split("\n")
seen = defaultdict(int)

def get_arrangements(s):
    if s in seen:
        return seen[s]
    if s == "":
        return 1
    seen[s] = sum(get_arrangements(s[len(p):]) for p in patterns if s.startswith(p))
    return seen[s]

print("Answer A:", sum(get_arrangements(design) > 0 for design in designs) )
print("Answer B:", sum(get_arrangements(design) for design in designs))
