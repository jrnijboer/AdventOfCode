def solve(inputValue):
    oc, ip, I = 0, 0, list(map(int,open("../input/day5.input").readline().split(",")))    
    while oc != 99:
        m1, m2 = I[ip] % 1000 // 100, I[ip] % 10000 // 1000
        val1 = I[ip + 1] if m1 == 1 else I[I[ip + 1]]
        if oc != 3 and oc != 4: val2 = I[ip + 2] if m2 == 1 else I[I[ip + 2]]
        if oc == 1: I[I[ip + 3]] = val1 + val2
        elif oc == 2: I[I[ip + 3]] = val1 * val2
        elif oc == 3: I[I[ip + 1]] = inputValue
        elif oc == 4 and val1 != 0: print(val1)
        elif oc == 5: ip = val2 - 2 if val1 != 0 else ip + 1
        elif oc == 6: ip = val2 - 2 if val1 == 0 else ip + 1
        elif oc == 7: I[I[ip + 3]]  = 1 if val1 < val2 else 0
        elif oc == 8: I[I[ip + 3]] = 1 if val1 == val2 else 0
        ip = ip + 4 if oc in [1,2,7,8] else ip + 2
        oc = I[ip] % 100
print("answer a: ", end = ''), solve(1)
print("answer b: ", end = ''), solve(5)