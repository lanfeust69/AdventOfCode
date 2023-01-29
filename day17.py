step = 328

# size, target = 2018, 2017
size, target = 50000001, 0

linked = [-1] * size
linked[0] = 0
cur = 0

for i in range(1, size):
    if i % 1000000 == 0:
        print(i)
    for _ in range(step):
        cur = linked[cur]
    linked[i] = linked[cur]
    linked[cur] = i
    cur = i

print(linked[target])
