values = list(map(int, open("../input/day1.input").readlines()))
print ("answer a:", sum(values))
f = 0;
freqs = set();
i = 0;
while True:
    f += values[i % len(values)]
    if f in freqs:
        break
    freqs.add(f)
    i += 1
print ("answer b:", f)
