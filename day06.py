blocks = (4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3)

n = len(blocks)

def redist(blocks):
    biggest, idx = -1, -1
    for i in range(n):
        if blocks[i] > biggest:
            biggest = blocks[i]
            idx = i
    new_blocks = list(blocks)
    new_blocks[idx] = 0
    for i in range(n):
        new_blocks[i] += biggest // n
    for i in range(biggest % n):
        new_blocks[(idx + 1 + i) % n] += 1
    return tuple(new_blocks)

seen = {blocks: 0}
steps = 0
while True:
    steps += 1
    blocks = redist(blocks)
    if blocks in seen:
        print(steps)
        print(steps - seen[blocks])
        break
    seen[blocks] = steps
