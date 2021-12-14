s = 0
for line in open('test.in'):
    patterns, data = line.split(' | ')
    patterns = [frozenset(x) for x in patterns.split()]
    data = [frozenset(x) for x in data.split()]

    one = next(p for p in patterns if len(p) == 2)
    seven = next(p for p in patterns if len(p) == 3)
    four = next(p for p in patterns if len(p) == 4)
    eight = next(p for p in patterns if len(p) == 7)
    six = next(p for p in patterns if len(p) == 6 and p & one != one)
    nine = next(p for p in patterns if len(p) == 6 and p & four == four)
    zero = next(p for p in patterns if len(p) == 6 and p != six and p != nine)
    three = next(p for p in patterns if len(p) == 5 and p & one == one)
    five = next(p for p in patterns if len(p) == 5 and p & six == p)
    two = next(p for p in patterns if len(p) == 5 and p != three and p != five)

    mapping = {zero: 0, one: 1, two: 2, three: 3, four: 4, five: 5, six: 6, seven: 7, eight: 8, nine: 9}

    v = 0
    for d in data:
        v = v * 10 + mapping[d]
    s += v

print(s)
