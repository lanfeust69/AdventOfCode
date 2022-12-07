nb1, nb2 = 0, 0
for line in open('test.in'):
    first, second = line.split(',')
    start1, end1 = map(int, first.split('-'))
    start2, end2 = map(int, second.split('-'))
    if (start1 >= start2 and end1 <= end2) or (start1 <= start2 and end1 >= end2):
        nb1 += 1
    if (start1 <= start2 <= end1) or (start2 <= start1 <= end2):
        nb2 += 1

print(nb1, nb2)
