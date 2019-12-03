def getRoute (directions):
    route, p = [], [0, 0]
    for d in directions.split(","):
        D, steps = d[0], int(d[1:])
        while steps > 0:
            if D == "U": p[1] += 1
            if D == "R": p[0] += 1
            if D == "L": p[0] -= 1
            if D == "D": p[1] -= 1
            steps -= 1
            route.append((p[0], p[1]))
    return route

input = open("../input/day3.input").readlines()
r1, r2 = getRoute(input[0]), getRoute(input[1])
intersect = set(r1).intersection(set(r2))
a = min(intersect, key=lambda x:abs(x[0]) + abs(x[1]))
print("answer a: {}".format(abs(a[0]) + abs(a[1])))
print("answer b: {}".format(2 + min([r1.index(i) + r2.index(i) for i in intersect])))