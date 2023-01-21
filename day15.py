disks = [(5, 4), (2, 1)]
disks = [(13, 11), (5, 0), (17, 11), (3, 0), (7, 2), (19, 17)]
disks = [(13, 11), (5, 0), (17, 11), (3, 0), (7, 2), (19, 17), (11, 0)]

n = 1
sizes = []
targets = []
step = 0
for x, p in disks:
    sizes.append(x)
    n *= x
    step += 1
    targets.append(-(step + p) % x)

res = 0
for i in range(len(disks)):
    nn = n // sizes[i]
    v = pow(nn, -1, sizes[i])
    res += v * nn * targets[i]

print(res % n)
