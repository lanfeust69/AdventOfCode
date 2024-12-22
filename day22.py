from collections import deque

seeds = [int(line.rstrip()) for line in open('test.in')]

def pseudo_random(n):
    n = ((n << 6) ^ n) & ((1 << 24) - 1)
    n = ((n >> 5) ^ n) & ((1 << 24) - 1)
    n = ((n << 11) ^ n) & ((1 << 24) - 1)
    return n

res = 0
by_deltas = {}
for seed in seeds:
    seen = set()
    n = seed
    prev = n % 10
    deltas = deque()
    for _ in range(2000):
        n = pseudo_random(n)
        price = n % 10
        deltas.append(price - prev)
        if len(deltas) > 4:
            deltas.popleft()
        if len(deltas) == 4:
            key = (deltas[0], deltas[1], deltas[2], deltas[3])
            if key not in seen:
                seen.add(key)
                if key not in by_deltas:
                    by_deltas[key] = price
                else:
                    by_deltas[key] += price
        prev = price
    res += n

print(res)
print(max(by_deltas.values()))
