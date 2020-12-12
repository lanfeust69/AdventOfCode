inf, sup = 264793, 803935

def gen(current):
    if len(current) == 6:
        if sum(1 for i in range(5) if current[i] == current[i + 1] and (i == 0 or current[i] != current[i - 1]) and (i == 4 or current[i] != current[i + 2])) > 0:
            candidate = sum(current[i]*10**(5 - i) for i in range(6))
            if inf <= candidate <= sup:
                yield candidate
    else:
        start = 0 if len(current) == 0 else current[-1]
        for n in range(start, 10):
            for v in gen(current[:] + [n]):
                yield v

print(sum(1 for _ in gen([])))
