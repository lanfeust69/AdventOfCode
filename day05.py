from bisect import bisect

in_intervals = True
intervals = []
starts, ends = {}, {}
queries = []
for line in open('test.in'):
    line = line.rstrip()
    if not line:
        in_intervals = False
        continue
    if in_intervals:
        start, end = map(int, line.split('-'))
        end += 1
        intervals.append((start, end))
        if start in starts:
            starts[start] += 1
        else:
            starts[start] = 1
        if end in ends:
            ends[end] += 1
        else:
            ends[end] = 1
    else:
        queries.append(int(line))

points = sorted(starts | ends)
nb_covering = [0] * len(points)
nb = 0
for i, p in enumerate(points):
    if p in starts:
        nb += starts[p]
    if p in ends:
        nb -= ends[p]
    nb_covering[i] = nb

def find_nb_covering(x):
    if x < points[0]:
        return 0
    if x >= points[-1]:
        return 0
    pos = bisect(points, x) - 1
    return nb_covering[pos]

res1 = sum(find_nb_covering(q) > 0 for q in queries)
print(res1)

res2 = 0
for i in range(1, len(nb_covering)):
    if nb_covering[i - 1] > 0:
        res2 += points[i] - points[i - 1]
print(res2)
