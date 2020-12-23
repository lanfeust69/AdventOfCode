def step(current):
    to_remove = []
    cur = linked[current]
    while len(to_remove) < 3:
        to_remove.append(cur)
        cur = linked[cur]
    dest = (current + mod - 1) % mod
    while dest in to_remove:
        dest = (dest + mod - 1) % mod
    keep = linked[dest]
    linked[dest] = to_remove[0]
    linked[current] = linked[to_remove[-1]]
    linked[to_remove[-1]] = keep
    return linked[current]

arr = [int(d) - 1 for d in '739862541']

for mod in [len(arr), 1000000]:
    linked = [i + 1 for i in range(mod)]
    for i in range(len(arr)):
        linked[i] = arr[(arr.index(i) + 1) % len(arr)]
    if mod > len(arr):
        linked[arr[-1]] = len(arr)
        linked[-1] = arr[0]
    current = arr[0]

    nb_steps = 100 if mod == len(arr) else 10000000
    for i in range(nb_steps):
        current = step(current)

    if mod == len(arr):
        p = 0
        to_print = ''
        for _ in range(mod - 1):
            to_print += str(linked[p] + 1)
            p = linked[p]
        print(to_print)
    else:
        a = linked[0]
        b = linked[a]
        print(a + 1, b + 1, (a + 1) * (b + 1))
