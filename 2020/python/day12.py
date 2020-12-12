input = [line.strip() for line in open("../input/day12.input").readlines()]
DD = {"N":(0,-1), "W":(-1,0), "S":(0,1), "E":(1,0)}
course, Pa, W, Pb = "E", (0, 0), (10, -1), (0,0)
for line in input:
  d, count = line[0], int(line[1:])
  if d in "NWSE":
    dx,dy = count * DD[d][0], count * DD[d][1]
    Pa = (Pa[0]+dx, Pa[1]+dy)
    W = (W[0]+dx, W[1]+dy)
  elif d == "F":
    dx,dy = count * DD[course][0], count * DD[course][1]
    Pa = (Pa[0]+dx, Pa[1]+dy)
    Pb = (Pb[0]+count * W[0], Pb[1]+count * W[1])
  else:
    for _ in range(count//90): W = (W[1] * -1, W[0]) if d == "R" else (W[1], W[0] * -1)
    course = "NWSE"[("NWSE".index(course) - count//90) % 4] if d == "R" else "NWSE"[("NWSE".index(course) + count//90) % 4]
print("Answer A:", abs(Pa[0]) + abs(Pa[1]))
print("Answer B:", abs(Pb[0]) + abs(Pb[1]))
