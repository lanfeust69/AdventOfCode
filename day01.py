for line in open('test.in'):
    floor = 0
    pos = 0
    first = True
    for c in line.rstrip():
        pos += 1
        floor += 1 if c == '(' else -1
        if floor == -1 and first:
            print('first visit to basement :', pos)
            first = False

    print('final floor', floor)
