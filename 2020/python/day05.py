def getSeatId(seat):
  rowStep, rowLo, rowHi, colStep, colLo, colHi = 64, 0, 127, 4, 0, 7
  for r in range(10):
    if seat[r] == "F": rowHi -= rowStep
    elif seat[r] == "B": rowLo += rowStep
    elif seat[r] == "L": colHi -= colStep
    elif seat[r] == "R": colLo+= colStep
    if seat[r] in "FB": rowStep //= 2
    if seat[r] in "LR": colStep //= 2
  return rowLo * 8 + colLo

seats = [getSeatId(line) for line in open("../input/day05.input").readlines()]
print("Answer A:", max(seats))
print("Answer B:", [r * 8 + c for c in range(1,6) for r in range(len(seats) // 8) if r * 8 + c not in seats and  r * 8 + c - 1 in seats and  r * 8 + c + 1 in seats][0])
