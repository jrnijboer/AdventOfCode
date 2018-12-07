import re
guards = dict()
guard, sleep = 0, 0
for line in sorted(open("../input/day4.input").readlines()):    
    m = re.search("^\[(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})\] (Guard|falls|wakes) (#\d+)?", line)
    if m.group(6) == "Guard":
        guard = int(m.group(7)[1:])
        if not guard in guards:
            guards[guard] = dict()
    elif m.group(6) == "falls":
        sleep = int(m.group(5))
    elif m.group(6) == "wakes":
        wakes = int(m.group(5))
        for i in range(wakes-sleep):
            if not i + sleep in guards[guard]:
                guards[guard][i+sleep] = 1
            else:
                guards[guard][i+sleep] += 1
guards = {key:val for key, val in guards.items() if len(val) > 0}

guard = sorted(guards, key=lambda g: sum(guards[g].values()), reverse=True)[0]
minute = sorted(guards[guard], key=guards[guard].get, reverse=True)[0]
print("day4, answer a: ", guard * minute)

guard = sorted(guards, key=lambda g: max(guards[g].values()), reverse=True)[0]
minute = sorted(guards[guard], key=guards[guard].get, reverse=True)[0]
print("day4, answer b: ", guard * minute)
