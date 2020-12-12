import sys
sys.stdin = open('test.in')

best = -1
seen = set()
for line in sys.stdin:
    id = 0
    for i in range(10):
        id *= 2 
        if line[i] == 'B' or line[i] == 'R':
            id += 1
    seen.add(id)

for seat in range(1, 1023):
    if seat not in seen and seat - 1 in seen and seat + 1 in seen:
        print(seat)
