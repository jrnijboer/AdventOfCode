from collections import deque

def play(players, marbles):
    scores = [0] * players
    Q = deque([0])
    for m in range(1, marbles + 1):
        if m % 23 == 0:
            Q.rotate(7)
            scores[m%players] += Q.pop() + m
            Q.rotate(-1)
        else:
            Q.rotate(-1)
            Q.append(m)
    return (max(scores))

input = list(open("../input/day9.input").readline().strip("\n").split(" "))
players, marbles = int(input[0]), int(input[6]) 
print("day 9, part a:", play(players, marbles))
print("day 9, part b:", play(players, marbles*100))
