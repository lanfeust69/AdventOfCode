import re

def cut(deck, n):
    return deck[n:] + deck[:n]

def rev(deck):
    return list(reversed(deck))

def incr(deck, n):
    res = [0] * len(deck)
    cur_out = 0
    for card in deck:
        res[cur_out] = card
        cur_out = (cur_out + n) % len(res)
    return res

# mod = 10007
mod = 119315717514047
def cut_mod(cur, n):
    return cur[0], (cur[1] + mod - n) % mod
def rev_mod(cur):
    return mod - cur[0], (mod * 2 - 1 - cur[1]) % mod
def incr_mod(cur, n):
    return (cur[0] * n) % mod, (cur[1] * n) % mod

# deck = list(range(mod))
cur = (1, 0)
for line in open('test.in'):
    if line[:-1] == 'deal into new stack':
        # deck = rev(deck)
        cur = rev_mod(cur)
        continue
    m = re.match(r'cut (-?\d+)', line)
    if m:
        # deck = cut(deck, int(m.group(1)))
        cur = cut_mod(cur, int(m.group(1)))
        continue
    m = re.match(r'deal with increment (\d+)', line)
    if m:
        # deck = incr(deck, int(m.group(1)))
        cur = incr_mod(cur, int(m.group(1)))

# sol = deck.index(2019)
# print(sol)
print(cur)
p = 101741582076661
pow_cur0 = pow(cur[0], p, mod)
pow_cur1 = (pow_cur0 + mod - 1) * pow((mod - 1 + cur[0]) % mod, mod - 2, mod) * cur[1] % mod
sol = 2020
print((sol + mod - pow_cur1) * pow(pow_cur0, mod - 2, mod) % mod)

# a(ax + b) + b = a²x + ab + b
# a(a²x + ab + b) + b = a³x + a²b + ab + b
# a^n.x + b(a^(n-1) + a^(n-2) + ... + a² + a + 1)
# a^n.x + b(a^n - 1)/(a - 1)
