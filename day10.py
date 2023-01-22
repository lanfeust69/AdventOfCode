puzzle = '230,1,2,221,97,252,168,169,57,99,0,254,181,255,235,167'
# lens = eval('[' + puzzle + ']')
rounds = 64
lens = [ord(c) for c in puzzle] + [17, 31, 73, 47, 23]

cur = list(range(256))
skip = 0
pos = 0
for _ in range(rounds):
    for l in lens:
        to_reverse = cur[:l]
        to_reverse.reverse()
        cur = to_reverse + cur[l:]
        shift = (l + skip) % len(cur)
        pos = (pos + shift) % len(cur)
        cur = cur[shift:] + cur[:shift]
        skip += 1

# 0 should be at pos instead
cur = cur[-pos:] + cur[:-pos]
# print(cur[0] * cur[1])
h = ''
for i in range(16):
    x = 0
    for j in range(i * 16, (i + 1) * 16):
        x ^= cur[j]
    d = hex(x)[2:]
    if len(d) < 2:
        d = '0' + d
    h += d

print(h)
