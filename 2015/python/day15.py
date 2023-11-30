capacities, durabilities, flavors, textures, calories = dict(), dict(), dict(), dict(), dict()
lines = [line.strip().split() for line in open("../2015/input/day15.input", encoding="utf-8").readlines()]
for line in lines:
    capacities[line[0][:-1]] = int(line[2][:-1])
    durabilities[line[0][:-1]] = int(line[4][:-1])
    flavors[line[0][:-1]] = int(line[6][:-1])
    textures[line[0][:-1]] = int(line[8][:-1])
    calories[line[0][:-1]] = int(line[10])

scoreA = 0
scoreB = 0
for frosting in range(0, 101):
    for candy in range(0, 101):
        if frosting + candy > 100:
            break
        for butterscotch in range(0, 101):
            if frosting + candy + butterscotch > 100:
                break
            for sugar in range(0, 101):
                if frosting + candy + butterscotch + sugar > 100:
                    break
                if frosting + candy + butterscotch + sugar < 100:
                    continue
                capacity = max(0, capacities["Frosting"] * frosting + capacities["Candy"] * candy + capacities["Butterscotch"] * butterscotch + capacities["Sugar"] * sugar)
                durability = max(0, durabilities["Frosting"] * frosting + durabilities["Candy"] * candy + durabilities["Butterscotch"] * butterscotch + durabilities["Sugar"] * sugar)
                flavor = max(0, flavors["Frosting"] * frosting + flavors["Candy"] * candy + flavors["Butterscotch"] * butterscotch + flavors["Sugar"] * sugar)
                texture = max(0, textures["Frosting"] * frosting + textures["Candy"] * candy + textures["Butterscotch"] * butterscotch + textures["Sugar"] * sugar)
                calory = max(0, calories["Frosting"] * frosting + calories["Candy"] * candy + calories["Butterscotch"] * butterscotch + calories["Sugar"] * sugar)
                score = capacity * durability * flavor * texture
                if calory == 500:
                    scoreB = max(score, scoreB)
                scoreA = max(score, scoreA)
print(scoreA)
print(scoreB)