stacks = []
for line in open('test.in'):
    if '[' in line:
        for i in range(len(line)):
            if line[i] == '[':
                stack = i // 4
                while len(stacks) <= stack:
                    stacks.append([])
                stacks[stack].append(line[i + 1])
    if line[:4] == 'move':
        _, nb, _, src, _, dest = line.split()
        nb, src, dest = map(int, [nb, src, dest])
        src, dest = src - 1, dest - 1 # 1-indexed, sigh...
        # for _ in range(nb):
        #     stacks[dest] = [stacks[src][0]] + stacks[dest]
        #     stacks[src] = stacks[src][1:]
        stacks[dest] = stacks[src][:nb] + stacks[dest]
        stacks[src] = stacks[src][nb:]

print(''.join(stack[0] if len(stack) else '' for stack in stacks))
