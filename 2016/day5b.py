import hashlib
code = 'ojvtpuvg'
p = '********'
n = 0 
h = ""
while '*' in p:
	s = ''.join([code, str(n)])
	m = hashlib.md5()
	m.update(s)
	h = m.hexdigest()
	if h.startswith('00000') and h[5] >= '0' and h[5] < '8' and p[int(h[5])] == '*':
		p = p[:int(h[5])] + h[6] + p[int(h[5]) + 1:]
		print p
	n += 1
