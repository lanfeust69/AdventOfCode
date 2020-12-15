init = [int(i) for i in '7,14,0,17,11,1,2'.split(',')]
spoken = {x: i for i, x in enumerate(init[:-1])}
last = init[-1]
for step in range(len(init) - 1, 30000000 - 1):
    if step % 1000000 == 0:
        print(step)
    if last in spoken:
        next = step - spoken[last]
    else:
        next = 0
    spoken[last] = step
    last = next

print(last)
