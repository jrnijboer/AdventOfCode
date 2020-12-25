def getLoopSize(pubkey):
  k, loops = 1, 0
  while k != pubkey:
    k *= 7
    k %= 20201227
    loops += 1
  return loops

k1, k2 = 8184785, 5293040
loop2 = getLoopSize(k2)
print("Final Answer:", pow(k1, loop2, 20201227))
