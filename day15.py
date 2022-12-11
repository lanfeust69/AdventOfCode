import itertools

ingredients = []
for line in open('test.in'):
    parts = line.split()
    ingredients.append(tuple([int(parts[2 + i * 2][:-1]) for i in range(4)] + [int(parts[-1])]))

n = len(ingredients)
res = 0
for cuts in itertools.combinations(range(1, 100), n - 1):
    quantities = [cuts[0]] + [cuts[i] - cuts[i - 1] for i in range(1, n - 1)] + [100 - cuts[-1]]
    sums = [0] * 5
    for i in range(n):
        for j in range(5):
            sums[j] += quantities[i] * ingredients[i][j]
    if min(sums) <= 0 or sums[-1] != 500:
        continue
    score = 1
    for s in sums[:-1]:
        score *= s
    res = max(res, score)

print(res)
