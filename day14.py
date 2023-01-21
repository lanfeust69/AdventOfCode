import hashlib

seed = 'cuanljph'
stretch = True

def stream():
    p = 0
    while True:
        h = hashlib.md5((seed + str(p)).encode()).hexdigest()
        if stretch:
            for _ in range(2016):
                h = hashlib.md5(h.encode()).hexdigest()
        p += 1
        yield h

triples = {hex(i)[-1]: [] for i in range(16)}
keys = []
index = 0
for h in stream():
    if len(keys) >= 64 and keys[63] < index - 1000:
        break
    h_triple = ''
    for i in range(len(h) - 2):
        if h[i + 1] != h[i] or h[i + 2] != h[i]:
            continue
        if not h_triple:
            h_triple = h[i]
            triples[h_triple].append(index)
        if i >= len(h) - 5 or h[i + 3] != h[i] or h[i + 4] != h[i]:
            continue
        for idx in triples[h[i]]:
            if index - 1000 <= idx < index:
                keys.append(idx)
        triples[h[i]] = [index] if h[i] == h_triple else []
    index += 1

print(keys[63])
