import itertools

sieve = [True] * 2000
primes = [2]
p = 3
while p < len(sieve):
    if sieve[p]:
        primes.append(p)
        for i in range(3, (len(sieve) - 1) // p, 2):
            sieve[p * i] = False
    p += 2

found1, found2 = False, False
for nn in range(3, 3000000):
    n = nn
    decomp = []
    for p in primes:
        if p * p > n:
            break
        pp = 0
        while n % p == 0:
            n //= p
            pp += 1
        if pp > 0:
            decomp.append((p, pp))
    if n > 1:
        decomp.append((n, 1))
    sum_divs1, sum_divs2 = 0, 0
    for powers in itertools.product(*map(lambda x: range(x[1] + 1), decomp)):
        divisor = 1
        for i in range(len(decomp)):
            divisor *= pow(decomp[i][0], powers[i])
        sum_divs1 += divisor
        if nn // divisor <= 50:
            sum_divs2 += divisor
    if not found1 and sum_divs1 * 10 >= 29000000:
        print(nn)
        found1 = True
    if not found2 and sum_divs2 * 11 >= 29000000:
        print(nn)
        found2 = True
    if found1 and found2:
        break
