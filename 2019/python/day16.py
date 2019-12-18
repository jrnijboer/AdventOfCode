import collections
input = [int(s) for s in open("../input/day16.input").readline().strip()]
base, S, size = [0, 1, 0, -1], [], len(input)

for i in range(size):
    ix, s = 0, []
    while len(s) <= size:
        for j in range(i+1): s.append(base[ix])
        ix = (ix + 1) % 4
    S.append(s[1:size+1])

def fft(input):
    s = []
    for i in range(size):
        k = 0
        for j in range(size): k += input[j] * S[i][j]
        s.append(abs(k) % 10)
    return s

for i in range(100): input = fft(input)
print("answer a: ", ''.join(map(str, input))[:8])

input = open("../input/day16.input").readline().strip()
input = input * 10000
offset = int(''.join(map(str, input))[:7])
input = [int(s) for s in input[offset:]]

for i in range(100):
    next, sum = collections.deque(), 0
    for j in range(len(input), 0, -1 ):
        sum += input[j - 1]
        next.appendleft(sum % 10)
    input = list(next)
print("answer b: ", ''.join(map(str, input))[:8])