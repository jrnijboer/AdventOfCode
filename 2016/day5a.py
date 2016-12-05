import hashlib
code = 'ojvtpuvg'
p = ''
n = 0
for i in range(0,8):
    h = "123456"
    while h[:5] != "00000":
        s = ''.join([code, str(n)])
        m = hashlib.md5()
        m.update(s)
        h = m.hexdigest()
        n += 1
    p += h[5]
print p
