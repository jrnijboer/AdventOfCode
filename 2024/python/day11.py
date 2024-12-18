from collections import defaultdict, Counter
stones_dict = Counter([int(part) for part in open ("../input/11.txt", encoding="utf-8").read().strip().split(" ")])

def blink(stones, blinkcount):
    for _ in range(blinkcount):
        next_stones = defaultdict(int)
        for val, cnt in stones.items():
            if val == 0:
                next_stones[1] += cnt
            elif len(str(val)) % 2 == 0:
                p1, p2 = str(val)[:len(str(val))//2], str(val)[len(str(val))//2:]
                next_stones[int(p1)] += cnt
                next_stones[int(p2)] += cnt
            else:
                next_stones[val*2024] += cnt
        stones = next_stones
    return stones

stones_dict = blink(stones_dict, 25)
print("Answer A:", sum(stones_dict.values()))
stones_dict = blink(stones_dict, 50)
print("Answer B:", sum(stones_dict.values()))
