input = open("../input/day8.input").readline().strip()
pixels = {i:'2' for i in range(150)}
layer = min([input[i:i+150] for i in range(0, len(input), 150)], key=lambda l : l.count('0'))
print("answer a: {}".format(layer.count('1') * layer.count('2')))
for pos in range(len(input)):
    if pixels[pos%150] == '2': pixels[pos%150] = ' ' if input[pos] == '0' else '#' if input[pos] == '1' else input[pos]
for kv in pixels.items(): print(kv[1], end='\n' if (kv[0] + 1) % 25 == 0 else '')