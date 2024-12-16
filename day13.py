import re

def extended_euclid(a, b):
    r0, r1, s0, s1 = a, b, 1, 0
    while r1 != 0:
        q = r0 // r1
        r0, r1, s0, s1 = r1, r0 - q * r1, s1, s0 - q * s1
    return r0, s0, (r0 - s0 * a) //b

# b = (x0 y - x y0) / (x0y1 - x1y0)
# a = (x - b x1) / x0
def solve(coefs):
    d = coefs[0][0] * coefs[1][1] - coefs[0][1] * coefs[1][0]
    n = coefs[0][0] * coefs[1][2] - coefs[0][2] * coefs[1][0]
    if d == 0:
        # apparently doesn't actually happen...
        if n == 0:
            # Y equation is a multiple of X equation : solve for X only
            xa, xb, x = coefs[0]
            g, u, v = extended_euclid(xa, xb)
            if x % g != 0:
                return 0
            xa, xb, x = xa // g, xb // g, x // g
            a, b = x * u, x * v
            if a < 0:
                k = -a // xb + 1
                a += k * xb
                b -= k * xa
            if b < 0:
                k = -b // xa + 1
                a -= k * xb
                b += k * xa
            if a >= 0 and b >= 0:
                if xa >= 3 * xb:
                    # minimize number or b
                    k = b // xa
                    a += k * xb
                    b -= k * xa
                else:
                    # minimize number or a
                    k = a // xb
                    a -= k * xb
                    b += k * xa
                return a * 3 + b
            return 0
        else:
            return 0
    if n % d != 0:
        return 0
    nb_b = n // d
    n = coefs[0][2] - nb_b * coefs[0][1]
    if n < 0 or n % coefs[0][0] != 0:
        return 0
    return n // coefs[0][0] * 3 + nb_b

coefs = [[0] * 3, [0] * 3]
res1, res2 = 0, 0
for line in open('test.in'):
    m = re.match(r'Button (A|B): X\+(\d+), Y\+(\d+)', line)
    if m:
        coefs[0][m.group(1) == 'B'] = int(m.group(2))
        coefs[1][m.group(1) == 'B'] = int(m.group(3))
    else:
        m = re.match(r'Prize: X=(\d+), Y=(\d+)', line)
        if m:
            coefs[0][2] = int(m.group(1))
            coefs[1][2] = int(m.group(2))
            res1 += solve(coefs)
            coefs[0][2] += 10000000000000
            coefs[1][2] += 10000000000000
            res2 += solve(coefs)

print(res1)
print(res2)
