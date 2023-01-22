n1, n2 = 0, 0
for line in open('test.in'):
    words = line.rstrip().split()
    seen1 = set()
    seen2 = set()
    ok1, ok2 = True, True
    for word in words:
        if word in seen1:
            ok1 = False
            ok2 = False
            break
        seen1.add(word)
        normalized = ''.join(sorted(c for c in word))
        if normalized in seen2:
            ok2 = False
        seen2.add(normalized)
    if ok1:
        n1 += 1
    if ok2:
        n2 += 1

print(n1, n2)
