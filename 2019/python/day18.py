from collections import defaultdict
import networkx as nx

def getDistances(I, topx, topy, bottomx, bottomy):
    deltas = [(0,1), (0,-1), (-1,0), (1,0)]
    Dkeys = defaultdict(list)
    Keys = {}
    PosKey = {}
    Locks = {}
    maze = nx.Graph()

    for y in range(topy, bottomy):
        for x in range(topx, bottomx):
            if I[y][x] != "#":
                if "a" <= I[y][x] <= "z" or I[y][x] == "@":
                    Keys[I[y][x]] = (x,y)
                    PosKey[x,y] = I[y][x]
                elif "A" <= I[y][x] <= "Z":
                    Locks[I[y][x]] = (x,y)
                for d in deltas:
                    if I[y + d[1]][x + d[0]] != "#":
                        maze.add_edge((x,y), (x+d[0], y+d[1]))

    for k1 in Keys:
        for k2 in Keys:
            if k1 != k2:
                path = nx.shortest_path(maze, Keys[k1],Keys[k2])
                locks = []
                for l in Locks.keys():
                    if Locks[l] in path:
                        locks.append(l)
                keys = []
                for pos in path:
                    if pos in PosKey.keys() and PosKey[pos] != k1 and PosKey[pos] != k2:
                        keys.append(PosKey[pos])
                length = nx.shortest_path_length(maze, Keys[k1],Keys[k2])
                Dkeys[k1].append((k2, length, locks, keys))
    return Dkeys, Keys

def getShortestRoute(DKeys, Keys, skipLocks=False):
    # start Q with all keys that are directly accessible (without passing through doors)
    # Q items: stepsDone, destination, distanceToDest, KeysVisitedInVisitedOrder, KeysVisitedAlphabeticOrder
    Q = [(0, route[0], route[1], {"@"}) for route in Dkeys["@"] if len(route[2]) == 0 or skipLocks]

    SEEN = {("@","@"): 0}
    shortest = 999999999
    while Q:
        #visit destination from queue
        next = Q.pop()
        totaldist = next[0] + next[2]
        currentKey = next[1]
        KeysObtained = next[3].copy()
        KeysObtained.add(currentKey)

        if len(KeysObtained) == len(Keys):
            shortest = min(shortest, totaldist)
        if ((currentKey, tuple(KeysObtained))) in SEEN.keys():
            if SEEN[(currentKey, tuple(KeysObtained))] < totaldist:
                continue

        SEEN[((currentKey, tuple(KeysObtained)))] = totaldist
        for destinations in Dkeys[currentKey]:
            dest = destinations[0]
            dist = destinations[1]
            keysRequired = destinations[2]
            if dest in KeysObtained:
                continue
            #check if keys needed are present
            reachable = True
            for k in keysRequired:
                if k.lower() not in KeysObtained:
                    reachable = False
                    break
            if reachable or skipLocks:
                Q.append((totaldist, dest, dist, KeysObtained))
    return shortest

I = open("../input/day18.input").readlines()
height, width = len(I), len(I[0].strip('\n'))
Dkeys, Keys = getDistances(I, 0, 0, width, height)
print("calculating part A will take several minutes...")
# print("Answer A:", getShortestRoute(Dkeys, Keys))

I = open("../input/day18-b.input").readlines()
partB = 0
#leftupper
Dkeys, Keys = getDistances(I, 0, 0, width//2, height//2)
partB += getShortestRoute(Dkeys, Keys, True)
#rightupper
Dkeys, Keys = getDistances(I, width//2, 0, width, height//2)
partB += getShortestRoute(Dkeys, Keys, True)
#leftbottom
Dkeys, Keys = getDistances(I, 0, height//2, width//2, height)
partB += getShortestRoute(Dkeys, Keys, True)
#rightbottom
Dkeys, Keys = getDistances(I, width//2, height//2, width, height)
partB += getShortestRoute(Dkeys, Keys, True)

print("Answer B:", partB)
