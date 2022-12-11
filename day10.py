def process(s):
    cur = s[0]
    nb = 1
    res = ''
    for c in s[1:]:
        if c == cur:
            nb += 1
        else:
            res += str(nb) + cur
            cur = c
            nb = 1
    res += str(nb) + cur
    return res

s = '1321131112'
for _ in range(50):
    s = process(s)

print(len(s))
