def getRoute (directions):
    delta = dict(zip('LRUD', [(-1, 0),(1, 0),(0, 1),(0, -1)]))
    route, p = [], [0, 0]
    for d in directions.split(","):
        D, steps = d[0], int(d[1:])
        while steps > 0:
            p = (p[0] + delta[D][0], p[1] + delta[D][1])
            steps -= 1
            route.append((p[0], p[1]))
    return route

input = open("../input/day3.input").readlines()
r1, r2 = getRoute(input[0]), getRoute(input[1])
intersect = set(r1).intersection(set(r2))
print("answer a: {}".format(min([abs(i[0]) + abs(i[1]) for i in intersect])))
print("answer b: {}".format(2 + min([r1.index(i) + r2.index(i) for i in intersect])))