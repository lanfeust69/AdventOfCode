for line in open('test.in'):
    for i in range(13, len(line)):
        ok = True
        for j in range(i - 13, i):
            for k in range(j + 1, i + 1):
                if line[j] == line[k]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            print(i + 1)
            break
