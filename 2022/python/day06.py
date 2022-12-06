s = open("../input/day06.input", encoding="utf-8").read().strip()
markers = [[ i + w for i in range(len(s)) if len(set(s[i : i + w])) == w] for w in [4, 14]]
print(f"Answer A: {markers[0][0]}\nAnswer B: {markers[1][0]}")
