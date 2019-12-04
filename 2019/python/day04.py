from itertools import groupby
def Part1Constraints(s):
    return any(i == j for i, j in zip(s, s[1:])) and ''.join(sorted(s)) == s

def Part2Constraints(s):
    pairs=[s[i] + s[i + 1] for i in range(len(s) - 1) if s[i] == s[i + 1]]
    return any([len(list(group)) == 1 for _, group in groupby(pairs)])

candidates = [i for i in range(240920,789857) if Part1Constraints(str(i))]
print("answer a: {}".format(len(candidates)))
print("answer b: {}".format(len([i for i in candidates if Part2Constraints(str(i))])))