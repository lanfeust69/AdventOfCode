# m = '2333133121414131402'
m = ''.join(line.rstrip() for line in open('test.in'))

id = 0
in_file = True
mem = []
free = []
files = []
for c in m:
    l = int(c)
    if in_file:
        files.append((len(mem), l))
        mem += [id] * l
        id += 1
    else:
        free.append((len(mem), l))
        mem += [-1] * l
    in_file = not in_file

mem_bak = mem[:]
start, end = 0, len(mem) - 1
while True:
    while mem[start] != -1:
        start += 1
    while mem[end] == -1:
        end -= 1
    if start > end:
        break
    mem[start], mem[end] = mem[end], mem[start]

res = 0
for i, id in enumerate(mem):
    if id != -1:
        res += i * id
print(res)

mem = mem_bak
first_free = 0
while free[first_free][1] == 0:
    first_free += 1
for id in range(len(files) - 1, -1, -1):
    pos, l = files[id]
    for j in range(first_free, len(free)):
        if free[j][0] >= pos:
            break
        if free[j][1] >= l:
            for k in range(l):
                mem[free[j][0] + k] = id
                mem[pos + k] = -1
            free[j] = free[j][0] + l, free[j][1] - l
            while free[first_free][1] == 0:
                first_free += 1
            break

res = 0
for i, id in enumerate(mem):
    if id != -1:
        res += i * id
print(res)
