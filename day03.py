def solve(bank, nb):
    n = len(bank)
    cache = [[-1] * nb for _ in range(n)]
    def inner(pos, remain):
        if remain == 0:
            return 0
        if cache[pos][remain - 1] != -1:
            return cache[pos][remain - 1]
        res = bank[pos] * 10**(remain - 1) + inner(pos + 1, remain - 1)
        if pos + remain < n:
            res = max(res, inner(pos + 1, remain))
        cache[pos][remain - 1] = res
        return res
    return inner(0, nb)

part1 = 0
part2 = 0
for line in open('test.in'):
    line = line.rstrip()
    bank = [int(c) for c in line]
    part1 += solve(bank, 2)
    part2 += solve(bank, 12)

print(part1)
print(part2)
