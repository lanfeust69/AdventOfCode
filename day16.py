seed = [c == '1' for c in '11101000110010100']
target = 35651584

def expand(s):
    return s + [False] + [not b for b in reversed(s)]

def cksum(s):
    if len(s) % 2:
        return s
    return cksum([not (s[i * 2] ^ s[i * 2 + 1]) for i in range(len(s) // 2)])

cur = seed
while len(cur) < target:
    cur = expand(cur)

print(''.join('1' if b else '0' for b in cksum(cur[:target])))
