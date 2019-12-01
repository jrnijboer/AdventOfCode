input = list(map(int, open("../input/day1.input").readlines()))
fA = [i//3 - 2 for i in input]
print("answer a: {}".format(sum(fA)))
fB = 0
for f in fA:    
    while f > 0:
        fB = fB + f
        f = f//3 - 2
print("answer b: {}".format(fB))