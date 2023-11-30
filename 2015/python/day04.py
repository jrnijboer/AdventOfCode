import hashlib
S = open("../input/day04.input", encoding="utf-8").read().strip()
i, A = 1, True
while True:
    s = hashlib.md5((S + str(i)).encode()).hexdigest()
    if s.startswith("00000") and A:
        print("Answer A:", i)
        A = False
    elif s.startswith("000000"):
        print("Answer B:", i)
        break
    i += 1
