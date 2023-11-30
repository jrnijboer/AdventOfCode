import math
target = int(open("../2015/input/day20.input", encoding="utf-8").read())

def getDivisors(number):
    divisors = []
    for p in range(1, int(math.sqrt(number))):
        if number % p == 0:
            divisors.append(p)
            divisors.append(number // p)
    return divisors

housenumber = 1
while True:
    divisors = getDivisors(housenumber)
    presents = 10 * sum(divisors)
    if presents >= target:
        print("Answer A:", housenumber)
        break
    housenumber += 1

while True:
    divisors = [divisor for divisor in getDivisors(housenumber) if housenumber // divisor <= 50]
    presents = 11 * sum(divisors)
    if presents >= target:
        print("Answer B:", housenumber)
        break
    housenumber += 1
