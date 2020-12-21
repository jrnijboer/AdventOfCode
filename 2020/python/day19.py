import re
def solve(extendForB):
  rules, input = [line.strip() for line in open("../input/day19.input").read().split("\n\n")]
  rules = {k : v.split(" ") for k,v in  [r.split(": ") for r in rules.split("\n")]}
  if extendForB:
    rules["8"] = ["42", "{1,}"]
    rules["11"] = ["42", "{1}", "31", "{1}", "|", "42", "{2}", "31", "{2}", "|", "42", "{3}", "31", "{3}", "|", "42", "{4}", "31", "{4}"]

  Q = [k for k,v in rules.items() if v == ['"a"'] or v == ['"b"']]
  while Q:
    q = Q.pop(0)
    for k, v in rules.items():
      found = False
      for j, elem in enumerate(v):
        if elem == q:
          found = True
          rules[k][j] = ' '.join(["("] + rules[q] + [")"])
      if found and not any(v.isnumeric() for v in rules[k]) and k != "0":
        Q.append(k)
    del rules[q]
  pattern = "^" + ''.join(rules["0"]).replace(" ", "").replace('"', '') + "$"
  return len([line for line in input.split("\n") if re.search(pattern, line)])

print("Answer A:", solve(False))
print("Answer B:", solve(True))
