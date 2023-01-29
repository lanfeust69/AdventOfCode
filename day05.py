for line in open('test.in'):
    puzzle = [ord(c) for c in line.rstrip()]

def collapse(poly):
    res = []
    for c in poly:
        if len(res) > 0 and abs(c - res[-1]) == 32:
            res.pop()
        else:
            res.append(c)
    return res

print(len(collapse(puzzle)))

best = len(puzzle)
for letter in range(65, 91):
    best = min(best, len(collapse([c for c in puzzle if c != letter and c != letter + 32])))

print(best)
