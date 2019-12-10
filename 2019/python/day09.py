def solve(invalue, I, ip):
    offset, oc = 0, I[ip] % 100
    while oc != 99:
        m1, m2, m3 = I[ip] % 1000 // 100, I[ip] % 10000 // 1000, I[ip] // 10000
        val1 = I[I[ip + 1]] if m1 == 0 else I[ip + 1] if m1 == 1 else I[I[ip + 1] + offset]
        if oc not in [3,4,9]: val2 = I[I[ip + 2]] if m2 == 0 else I[ip + 2] if m2 == 1 else I[I[ip + 2] + offset]
        if oc == 1:
            if m3 == 0: I[I[ip + 3]] = val1 + val2
            else: I[I[ip + 3] + offset] = val1 + val2
        elif oc == 2:
            if m3 == 0: I[I[ip + 3]] = val1 * val2
            else: I[I[ip + 3] + offset] = val1 * val2
        elif oc == 3:
            if m1 == 0: I[I[ip + 1]] = invalue
            else: I[I[ip + 1] + offset] = invalue
        elif oc == 4 : return val1
        elif oc == 5: ip = val2 - 2 if val1 != 0 else ip + 1
        elif oc == 6: ip = val2 - 2 if val1 == 0 else ip + 1
        elif oc == 7:
            if m3 == 0: I[I[ip + 3]] = 1 if val1 < val2 else 0
            else: I[I[ip + 3] + offset] = I[I[ip + 3]] = 1 if val1 < val2 else 0
        elif oc == 8:
            if m3 == 0: I[I[ip + 3]] = 1 if val1 == val2 else 0
            else: I[I[ip + 3] + offset] = 1 if val1 == val2 else 0
        elif oc == 9: offset += val1
        ip = ip + 4 if oc in [1,2,7,8] else ip + 2
        oc = I[ip] % 100

I = list(map(int,open("../input/day9.input").readline().split(",")))
D1 = D2 = {i:I[i] for i in range(len(I))}
print("answer a: {}".format(solve(1, D1, 0)))
print("answer b: {}".format(solve(2, D2, 0)))
