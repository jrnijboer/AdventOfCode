instructions = open("../input/day22.input").readlines()

def dealIncrement(stack, inc):
    s = list(stack)
    for i in range(len(stack)): s[(inc * i) % len(s)] = stack[i]
    return s

s = list(range(10007))
for inst in instructions:
    if inst.startswith("deal into new stack"):
        s.reverse()
    elif inst.startswith("cut"):
        n = int(inst.strip("cut "))
        s = s[n:] + s[:n]
    elif inst.startswith("deal with increment"):
        n = int(inst.strip("deal with increment "))
        s = dealIncrement(s, n)
for i in range(len(s)):
    if s[i] == 2019: print("anwer a: ", i)

# part 2
# explanation: https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbnkaju/
#

decksize = 119315717514047
iterations = 101741582076661

(offset, increment) = (0, 1)
for inst in instructions:
    if inst.startswith("deal into new stack"):
        increment = (-increment) % decksize
        offset = (-offset - 1) % decksize
    elif inst.startswith("cut"):
        n = int(inst.strip("cut "))
        offset = (offset - n) % decksize
    elif inst.startswith("deal with increment"):
        n = int(inst.strip("deal with increment "))
        increment = (increment * n) % decksize
        offset = (offset * n) % decksize

offset_diff_per_run = offset
increment_mul_per_run = increment

def modularinverse(n, MOD):
    #only valid if MOD is prime
    return pow(n, MOD-2, MOD)

increment = pow(increment_mul_per_run, iterations, decksize)
offset = (offset_diff_per_run * (1 - pow(increment_mul_per_run, iterations, decksize)) * modularinverse(1 - increment_mul_per_run, decksize)) % decksize

print("answer b:", (modularinverse(increment, decksize) * (2020 - offset))%decksize)