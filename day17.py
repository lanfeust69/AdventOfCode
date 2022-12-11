sizes = [int(line) for line in open('test.in')]
sizes.sort(reverse=True)

n = len(sizes)
max_remain = [0] * n
max_remain[-1] = sizes[-1]
for i in range(n - 2, -1, -1):
    max_remain[i] = max_remain[i + 1] + sizes[i]

target = 150
cache = [[-1] * (target + 1) for _ in range(n)]
def solve(pos, remain):
    if remain == 0:
        return 1
    if pos == n:
        return 0
    if remain > max_remain[pos]:
        return 0
    if cache[pos][remain] != -1:
        return cache[pos][remain]
    res = solve(pos + 1, remain)
    if remain >= sizes[pos]:
        res += solve(pos + 1, remain - sizes[pos])
    cache[pos][remain] = res
    return res

print(solve(0, target))

cache2 = [[(-1, -1)] * (target + 1) for _ in range(n)]
def solve2(pos, remain):
    if remain == 0:
        return (1, 0)
    if pos == n:
        return (0, 0)
    if remain > max_remain[pos]:
        return (0, 0)
    if cache2[pos][remain] != (-1, -1):
        return cache2[pos][remain]
    nb_ways, nb_used = solve2(pos + 1, remain)
    if remain >= sizes[pos]:
        nb_ways_with, nb_used_with = solve2(pos + 1, remain - sizes[pos])
        if nb_ways_with > 0 and (nb_ways == 0 or nb_used_with + 1 < nb_used):
            nb_ways, nb_used = nb_ways_with, nb_used_with + 1
        elif nb_ways_with > 0 and nb_ways > 0 and nb_used_with + 1 == nb_used:
            nb_ways += nb_ways_with
    cache2[pos][remain] = nb_ways, nb_used
    return nb_ways, nb_used

print(solve2(0, target))
