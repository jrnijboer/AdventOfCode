def next_val():
    global ix, input
    ix += 1
    return input[ix -1]

def buildNode():   
    children, metadata = [], []
    cc, cm = next_val(), next_val() 
    for _ in range(cc):
        children.append(buildNode())
    for _ in range(cm):
        metadata.append(next_val())
    return children, metadata

def sumMeta(C, M):
    return sum(sumMeta(c[0], c[1]) for c in C) + sum(M)

def sumValue(C, M):
    return sum(M) if len(C) == 0 else sum(sumValue(C[m-1][0], C[m-1][1]) for m in M if m > 0 and m <= len(C))

input = list(map(int, open("../input/day8.input").readline().strip("\n").split(" ")))
ix = 0
root = buildNode()
print("day 8, part a:", sumMeta(root[0], root[1]))
print("day 8, part b:", sumValue(root[0], root[1]))