file = open('test.in')
start = int(file.readline())
buses = [0 if x == 'x' else int(x) for x in file.readline().split(',')]
# buses = [0 if x == 'x' else int(x) for x in '7,13,x,x,59,x,31,19'.split(',')]

best_wait = max(buses)
res = 0
for bus in buses:
    if bus == 0:
        continue
    wait = (bus - start % bus) % bus
    if wait < best_wait:
        best_wait = wait
        res = bus * wait

print(res)

def gcd(a, b): return a if b == 0 else gcd(b, a % b)
def ext_euc(a, b):
    r0, u0, v0, r1, u1, v1 = a, 1, 0, b, 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, u0, v0, r1, u1, v1 = r1, u1, v1, r0 - q * r1, u0 - q * u1, v0 - q * v1
    return r0, u0, v0

lcm = 1
for bus in buses:
    if bus != 0:
        lcm = lcm * bus // gcd(lcm, bus)

sol = 0
for i, bus in enumerate(buses):
    if bus == 0:
        continue
    r, u, v = ext_euc(bus, lcm // bus)
    assert(r == 1)
    sol += (bus - i) * v * lcm // bus

while sol > lcm:
    sol -= lcm
while sol < 0:
    sol += lcm

print(sol)
