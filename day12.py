negatives = [False] * 2
positives = []
rules = {}

for line in open('test.in'):
    if line.startswith('init'):
        positives = [c == '#' for c in line.rstrip()[15:]]
        continue
    parts = line.rstrip().split(' => ')
    if len(parts) == 2:
        rules[parts[0]] = parts[1]

def get_val(pos):
    if pos >= 0:
        return positives[pos] if pos < len(positives) else 0
    pos = -pos - 1
    return negatives[pos] if pos < len(negatives) else 0

def set_val(pos, val):
    if pos >= 0:
        while len(positives) <= pos:
            positives.append(False)
        positives[pos] = val
        return
    pos = -pos - 1
    while len(negatives) <= pos:
        negatives.append(False)
    negatives[pos] = val

stab_step, stab_idx = -1, -1
for step in range(200):
    new_vals = []
    start = -len(negatives) - 2
    s = ''.join('#' if get_val(x) else '.' for x in range(start - 3, start + 2))
    for pos in range(start, len(positives) + 2):
        s = s[1:] + ('#' if get_val(pos + 2) else '.')
        new_val = (rules[s] if s in rules else '.') == '#'
        if get_val(pos) != new_val:
            new_vals.append((pos, new_val))
    for pos, val in new_vals:
        set_val(pos, val)
    if step == 19:
        print(sum(i for i in range(-len(negatives), len(positives)) if get_val(i)))
    if all(not v for v in negatives):
        idx = positives.index(True)
        if stab_step == -1 and len(positives) >= idx + 24 * 6 + 1 and positives[idx:idx + 24 * 6 + 1] == [True, False, False, True, True, False] * 24 + [True] and all(not v for v in positives[idx + 24 * 6 + 1:]):
            print('stabilized at step', step, 'first at', idx)
            val = sum(i for i in range(-len(negatives), len(positives)) if get_val(i))
            print('sum is then', val)
            stab_step, stab_idx, stab_val = step, idx, val

print(sum(i for i in range(-len(negatives), len(positives)) if get_val(i)))

delta = 199 - stab_step
print(stab_val + delta * 73)

delta = 49999999999 - stab_step
print(stab_val + delta * 73)
