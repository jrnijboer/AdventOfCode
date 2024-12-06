part1, part2 = open("../input/05.txt", encoding="utf-8").read().split("\n\n")
A, B = 0, 0
rules = [[int(x) for x in line.split("|")] for line in part1.splitlines()]
pages = [[int(x) for x in page.split(",")] for page in part2.splitlines()]

for page in pages:
    page_modified = False
    while any(l in page and r in page and page.index(l) > page.index(r) for l, r in rules):
        for l, r in rules:
            if l in page and r in page and page.index(l) > page.index(r):
                page[page.index(l)], page[page.index(r)] = page[page.index(r)], page[page.index(l)]
                page_modified = True

    A += 0 if page_modified else page[len(page) // 2]
    B += page[len(page) // 2] if page_modified else 0

print("Answer A:", A)
print("Answer B:", B)
