lines = open("../input/day6.input").readlines()
coords = dict()
minx, miny = 1e6, 1e6
maxx, maxy, safePositions = 0, 0, 0
closedAreas = dict()

for i in range(len(lines)):
    s = lines[i].split(",")    
    coords[i] = [int(s[0]), int(s[1])]
    minx = min(int(s[0]), minx)
    miny = min(int(s[1]), miny)
    maxx = max(int(s[0]), maxx)
    maxy = max(int(s[1]), maxy)
    closedAreas[i] = 0

for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        minDistance, sumDistance = 1e6, 0
        closestNodes= []        
        for p in coords:            
            distance = abs(x - coords[p][0]) + abs(y - coords[p][1])
            if distance < minDistance:
                minDistance = distance
                closestNodes = [ p ]
            elif distance == minDistance:
                closestNodes.append(p)
            sumDistance += distance

        closedAreas[closestNodes[0]]+=1
        if sumDistance < 10000:
            safePositions += 1

infAreas = [k for k, v in coords.items() if v[0] == minx or v[0] == maxx or v[1] == miny or v[1] == maxy]
closedAreas = {k:v for k, v in closedAreas.items() if k not in infAreas}

print ("day 6 part a:", max(closedAreas.values()))
print ("day 6 part b:", safePositions)
