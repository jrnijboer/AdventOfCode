number = open("../input/day10.input", encoding="utf-8").read().strip()
N = {}
for i in range(50):
    hearandsay = ""
    i = 0
    while i < len(number):
        n = number[i]
        count = 1
        while i + 1 < len(number) and number[i + 1] == n:
            i += 1
            count += 1
        i += 1
        hearandsay += str(count) + n
    number = hearandsay
    if i == 40: print("Answer A:", len(number))
print("Answer B:", len(number))
