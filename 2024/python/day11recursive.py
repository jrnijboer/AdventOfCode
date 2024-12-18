stones = [int(part) for part in open ("../input/11.txt", encoding="utf-8").read().strip().split(" ")]
cache = {}

def blink(stone, blinkcount):
    if (stone, blinkcount) in cache:
        return cache[(stone, blinkcount)]
    if blinkcount == 0:
        return 1
    elif stone == 0:
        result = blink(1, blinkcount-1)
    elif len(str(stone)) % 2 == 0:
        p1, p2 = str(stone)[:len(str(stone))//2], str(stone)[len(str(stone))//2:]
        result = blink(int(p1), blinkcount-1) + blink(int(p2), blinkcount-1)
    else:
        result = blink(stone*2024, blinkcount-1)
    cache[(stone, blinkcount)] = result
    return result

print("Answer A:", sum(blink(stone, 25) for stone in stones))
print("Answer B:", sum(blink(stone, 75) for stone in stones))
