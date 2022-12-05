from collections import defaultdict
input = open("../input/day05.input").readlines()
stacksA, stacksB = defaultdict(list), defaultdict(list)
columns = len(input[0]) // 4
A, B = "", ""

for line in input:
    if line.startswith("[") or line.startswith(" "):
        for n in range(columns):
            if 'A' <= line[n * 4 + 1] <= 'Z':
               stacksA[n + 1].insert(0, line[n * 4 + 1])
               stacksB[n + 1].insert(0, line[n * 4 + 1])    
    elif line.startswith("move"):
        count, src, dest = [int(x) for x in line.strip().split() if x.isnumeric()]        
        for n in range(count):
            stacksA[dest].append(stacksA[src].pop())
        stacksB[dest] += stacksB[src][count * -1:]
        stacksB[src] = stacksB[src][:-1 * count]

print(f"Answer A:", "".join([stacksA[k][-1] for k in sorted(stacksA.keys())]))
print(f"Answer B:", "".join([stacksB[k][-1] for k in sorted(stacksB.keys())]))
