from collections import defaultdict
lines = open("../input/day07.input", encoding="utf-8").readlines()
dirs, path = defaultdict(int), ["/"]

for parts in [line.split() for line in lines]:
    if parts[1] == "cd":
        path = path[:-1] if parts[2] == ".." else path + [parts[2]]
    elif parts[0].isnumeric():
        for i in range(len(path) + 1):
            dirs["/".join(path[:i])] += int(parts[0])

print("Answer A:", sum([v for v in dirs.values() if v < 100000]))
print("Answer B:", min([v for v in dirs.values() if v > 30000000 - (70000000 - max(dirs.values()))]))
