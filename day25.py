nums = [line.rstrip() for line in open('test.in')]

def from_snafu(s):
    v = 0
    b = 1
    for c in s[::-1]:
        if c == '=':
            v -= b * 2
        elif c == '-':
            v -= b
        else:
            v += int(c) * b
        b *= 5
    return v

def to_snafu(n):
    s = ''
    while n != 0:
        d = n % 5
        n //= 5
        if d < 3:
            s = str(d) + s
        else:
            s = ('=' if d == 3 else '-') + s
            n += 1
    return s

print(to_snafu(sum(map(from_snafu, nums))))
