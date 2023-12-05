import math
seeds, *maps = [line.strip() for line in open("../input/day05.txt", encoding="utf-8").read().split("\n\n")]
seeds, locations = [int(x) for x in seeds.split(" ")[1:]], []
rmaps = list(reversed(maps))
seedPairs = [(seeds[i],seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

def findDestFromMap(inVal, map): #search top to bottom
    for line in map.split("\n")[1:]:
        trgt, src, rnge = [int(x) for x in line.split(" ")]
        if src <= inVal <= src + rnge:
            return trgt - src + inVal
    return inVal

def findSourcesFromMap(inVal, map): #search from bottom to top
    for line in map.split("\n")[1:]:
        trgt, src, rnge = [int(x) for x in line.split(" ")]
        if trgt <= inVal <= trgt + rnge:
            return inVal - trgt + src
    return inVal

def getLowerBound(dest, stepSize) :
    while True:
        loc = dest
        for map in rmaps:
            loc = findSourcesFromMap(loc, map)
        for a,b in seedPairs:
            if loc  >= a and loc <= b:
                return dest
        dest += stepSize

# Part A
for seed in seeds:
    for m in maps:
        seed = findDestFromMap(seed, m)
    locations.append(seed)

# Part B, first increase step fom 0 by 1 milllion, step back last step, divide stepsize by 10, repeat
lowerBound, stepsize = 0, 10**math.floor(math.log(min([b - a for (a, b) in seedPairs]), 10))
while (stepsize > 0):
    lowerBound = getLowerBound(lowerBound, stepsize) - stepsize
    stepsize //= 10

print(f"Answer A: {min(locations)}")
print(f"Answer B: {lowerBound + 1}")
