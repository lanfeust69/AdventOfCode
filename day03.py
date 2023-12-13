engine = []
for line in open('test.in'):
    engine.append([c for c in line.rstrip()])

h, w = len(engine), len(engine[0])
res2 = 0
parts = {}
for r in range(h):
    for c in range(w):
        gear_parts = {}
        if engine[r][c] == '.' or engine[r][c].isdigit():
            continue
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                rr, cc = r + dr, c + dc
                if not (0 <= rr < h and 0 <= cc < w):
                    continue
                if not engine[rr][cc].isdigit():
                    continue
                start, end = cc, cc
                while start > 0 and engine[rr][start - 1].isdigit():
                    start -= 1
                while end < w and engine[rr][end].isdigit():
                    end += 1
                v = int(''.join(engine[rr][start:end]))
                parts[(rr, start)] = v
                gear_parts[(rr, start)] = v
        if engine[r][c] == '*' and len(gear_parts) == 2:
            p = 1
            for _, v in gear_parts.items():
                p *= v
            res2 += p

res = 0
for _, v in parts.items():
    res += v

print(res)
print(res2)
