password = open("../input/day11.input", encoding="utf-8").read().strip()
valid, alphabet = 0, "abcdefghijklmnopqrstuvwxyz"

def incrementpw(pw):
    l, ix = list(pw), 1
    while ix > 0 and ix < len(pw):
        if l[-ix] == "z":
            l[-ix] = "a"
            ix += 1
        else:
            l[-ix] = chr(ord(l[-ix]) + 1)
            ix = 0
    return "".join(l)

def isvalid(pw):
    if not any([ord(pw[i-2]) + 2 == ord(pw[i-1]) + 1 == ord(pw[i]) for i in range(len(pw)) if i >= 2]):
        return False

    if any([c in ["i", "l","o"] for c in pw]):
        return False

    return sum([1 for a, b in zip(alphabet, alphabet) if a + b in pw]) >= 2

while not isvalid(password):
    password = incrementpw(password)
print("Answer A:", password)

password = incrementpw(password)
while not isvalid(password):
    password = incrementpw(password)
print("Answer B:", password)
