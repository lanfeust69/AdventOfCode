all_files = {}
dir_sizes = {}
cur_path = []
for line in open('test.in'):
    tokens = line.rstrip().split()
    if tokens[0] == '$':
        if tokens[1] == 'cd':
            if tokens[2] == '..':
                cur_path = cur_path[:-1]
            else:
                cur_path.append(tokens[2])
        continue
    if tokens[0] == 'dir':
        continue
    all_files['/'.join(cur_path) + '/' + tokens[1]] = int(tokens[0])
    for l in range(1, len(cur_path) + 1):
        d = '/'.join(cur_path[:l])
        if d in dir_sizes:
            dir_sizes[d] += int(tokens[0])
        else:
            dir_sizes[d] = int(tokens[0])

used = dir_sizes['/']
needed = 30000000 - (70000000 - used)
res = used
for _, s in dir_sizes.items():
    if needed <= s < res:
        res = s

print(res)
