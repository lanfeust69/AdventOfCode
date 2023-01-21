for line in open('test.in'):
    s = line.rstrip()

def expand(s, recurse):
    res = 0
    pos = 0
    while pos < len(s):
        if s[pos] == '(':
            e_pos = s.index(')', pos + 1)
            nb, repeat = map(int, s[pos + 1:e_pos].split('x'))
            res += (expand(s[e_pos + 1:e_pos + 1 + nb], recurse) if recurse else nb) * repeat
            pos = e_pos + 1 + nb
        else:
            res += 1
            pos += 1
    return res

print(expand(s, False))
print(expand(s, True))
