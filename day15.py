def hash(s):
    cur = 0
    for c in s:
        cur = (cur + ord(c)) * 17 % 256
    return cur

lines = [line.rstrip() for line in open('test.in')]
res1 = 0
focals = {}
boxes = [[] for _ in range(256)]
for w in ''.join(lines).split(','):
    res1 += hash(w)
    if '=' in w:
        label, f = w.split('=')
        f = int(f)
    else:
        label, f = w[:-1], 0
    b = hash(label)
    focals[label] = f
    if f == 0 and label in boxes[b]:
        idx = boxes[b].index(label)
        boxes[b] = boxes[b][:idx] + boxes[b][idx + 1:]
    elif f != 0 and label not in boxes[b]:
        boxes[b].append(label)

res2 = 0
for b in range(256):
    for i in range(len(boxes[b])):
        res2 += (b + 1) * (i + 1) * focals[boxes[b][i]]

print(res1)
print(res2)
