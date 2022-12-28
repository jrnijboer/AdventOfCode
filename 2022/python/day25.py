lines = [line.strip() for line in open("/root/git/AdventOfCode/2022/input/day25.input", encoding="utf-8").readlines()]
SNAFUDEC = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
DECSNAFU = {2: "2", 1: "1", 0: "0", -1: "-", -2: "="}

def snafu_dec(s):
    return sum([5**(ix) * SNAFUDEC[c] for ix, c in enumerate(reversed(s))])

def dec_snafu(d):
    snafu = ""
    while d > 0:
        n = d % (5)
        if n > 2:
            n -= 5
        d = (d - n) // 5
        snafu = DECSNAFU[n] + snafu
    return snafu

snafu_sum = sum([snafu_dec(snafu) for snafu in lines])
print(dec_snafu(snafu_sum))
