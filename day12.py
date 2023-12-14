
def solve(springs, counts):
    nb = len(springs)
    total_damaged = sum(counts)
    cumul = [counts[0]]
    for i in range(1, len(counts)):
        cumul.append(cumul[-1] + counts[i])
    cumul.append(0) # hack for cumul[-1]
    cache = {}

    def dp(pos, group, group_pos):
        if pos == nb:
            return 1 if group == len(counts) and group_pos == 0 else 0
        if cumul[group - 1] + group_pos + nb - pos < total_damaged:
            return 0
        if group_pos > 0 and springs[pos] == '.':
            return 0
        if (pos, group, group_pos) in cache:
            return cache[(pos, group, group_pos)]
        if springs[pos] == '.':
            res = dp(pos + 1, group, group_pos)
            cache[(pos, group, group_pos)] = res
            return res
        if springs[pos] == '#' or group_pos > 0:
            if group == len(counts):
                return 0
            if group_pos == counts[group] - 1:
                if pos == nb - 1:
                    return 1 if group == len(counts) - 1 else 0
                if springs[pos + 1] == '#':
                    return 0
                res = dp(pos + 2, group + 1, 0) # +2 because at least one ok before next group
            else:
                res = dp(pos + 1, group, group_pos + 1)
            cache[(pos, group, group_pos)] = res
            return res
        # unknown at start
        res = 0
        # 1 - consider it damaged if possible
        if group < len(counts):
            if group_pos == counts[group] - 1:
                if pos == nb - 1:
                    res = 1 if group == len(counts) - 1 else 0
                elif springs[pos + 1] == '#':
                    res = 0
                else:
                    res = dp(pos + 2, group + 1, 0) # +2 because at least one ok before next group
            else:
                res = dp(pos + 1, group, group_pos + 1)
        # 2 - consider it ok
        res += dp(pos + 1, group, group_pos)
        cache[(pos, group, group_pos)] = res
        return res

    return dp(0, 0, 0)

res1, res2 = 0, 0
for line in open('test.in'):
    springs, counts = line.split()
    counts = list(map(int, counts.split(',')))
    res1 += solve(springs, counts)
    res2 += solve('?'.join([springs] * 5), counts * 5)

print(res1)
print(res2)
