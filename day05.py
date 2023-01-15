import hashlib

p = 0
pwd1 = ''
pwd2 = [''] * 8
needed = 8
while len(pwd1) < 8 or needed > 0:
    h = hashlib.md5(('reyedfim' + str(p)).encode()).hexdigest()
    if h.startswith('00000'):
        if len(pwd1) < 8:
            pwd1 += h[5]
        if h[5].isdigit():
            idx = int(h[5])
            if idx < len(pwd2) and pwd2[idx] == '':
                pwd2[idx] = h[6]
                needed -= 1
    p += 1

print(pwd1, ''.join(pwd2))
