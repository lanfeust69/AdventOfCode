puzzle = [int(line.rstrip()) for line in open('test.in')]

offsets = puzzle[:]
eip = 0
steps = 0
while eip < len(offsets):
    steps += 1
    new_eip = eip + offsets[eip]
    offsets[eip] += 1
    eip = new_eip

print(steps)

offsets = puzzle[:]
eip = 0
steps = 0
while eip < len(offsets):
    steps += 1
    new_eip = eip + offsets[eip]
    offsets[eip] += 1 if offsets[eip] < 3 else -1
    eip = new_eip

print(steps)
