def react (input):
    buffer = [input[0]]
    for i in range(1, len(input)):
        if len(buffer) > 0 and ord(buffer[-1]) ^ ord(input[i]) == 32:
            buffer.pop()
        else:
            buffer.append(input[i])
    buffer = ''.join(buffer)
    return len(buffer), buffer

input = open("../input/day5.input").readline().strip("\n")
minLength, buffer = react(input)
print("day5, answer a:", minLength)

for c in 'abcdefghijklmnopqrstuvwxyz':
    s = buffer
    res, _ = react(s.replace(c, "").replace(c.upper(), ""))
#    res, _ = react(s)
    minLength = min(res, minLength)
print("day5, answer b:", minLength)

