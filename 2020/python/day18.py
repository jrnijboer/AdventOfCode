input = [line.strip() for line in open("../input/day18.input").readlines()]

def toReversePolish(infix, usePrecedence):
  postfix, S = [], []
  for i in (("(" + infix + ")").replace("(", "( ").replace(")", " )")).split(" "):
    if i.isnumeric(): postfix += i
    elif i == "(": S.append(i)
    elif i in "+*":
      while S and S[-1] != "(" and ((usePrecedence and (i == "*" or (i == "+" and  S[-1] != "*"))) or not usePrecedence):
        postfix.append(S.pop())
      S.append(i)
    elif i == ")":
      while S and S[-1] != "(": postfix.append(S.pop())
      S.pop()
  return postfix

def calc(infix, usePrecedence):
  S, postfix = [], toReversePolish(infix, usePrecedence)
  for x in postfix:
    if x.isnumeric(): S.append(x)
    else: S.append(int(S.pop()) * int(S.pop()) if x == "*" else int(S.pop()) + int(S.pop()))
  return(S[0])

print("Answer A:", sum([calc(line, False) for line in input]))
print("Answer B:", sum([calc(line, True) for line in input]))
