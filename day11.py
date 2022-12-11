
def is_valid(s):
    has_seq = False
    for i in range(len(s) - 2):
        if ord(s[i + 1]) == ord(s[i]) + 1 and ord(s[i + 2]) == ord(s[i]) + 2:
            has_seq = True
            break
    if not has_seq:
        return False
    for first in range(len(s) - 3):
        if s[first] != s[first + 1]:
            continue
        for second in range(first + 2, len(s) - 1):
            if s[second] == s[second + 1]:
                return True
    return False

def incr(s):
    pos = len(s) - 1
    while s[pos] == 'z':
        pos -= 1
    c = chr(ord(s[pos]) + 1)
    if c in 'iol':
        c = chr(ord(c) + 1)
    return s[:pos] + c + 'a' * (len(s) - 1 - pos)

pwd = 'hepxxyzz'
for pos in range(len(pwd)):
    if pwd[pos] in 'iol':
        pwd = pwd[:pos] + chr(ord(pwd[pos]) + 1) + 'a' * (len(pwd) - 1 - pos)
        break

pwd = incr(pwd)
while not is_valid(pwd):
    pwd = incr(pwd)

print(pwd)
