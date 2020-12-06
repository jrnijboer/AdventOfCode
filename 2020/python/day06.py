input, b = [line for line in open("../input/day06.input").read().split("\n\n") if line ], 0
print("Answer A:", len([c for c in "abcdefghijklmnopqrstuvwxyz" for line in input if c in line]))
print("Answer B:", sum([len(set.intersection(*gset)) for gset in [[set(group) for group in line.split()] for line in input]]))
