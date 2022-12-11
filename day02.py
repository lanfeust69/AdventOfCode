total_paper = 0
total_ribbon = 0
for line in open('test.in'):
    dims = sorted(map(int, line.rstrip().split('x')))
    total_paper += dims[0] * dims[1] * 3 + dims[0] * dims[2] * 2 + dims[1] * dims[2] * 2
    total_ribbon += (dims[0] + dims[1]) * 2 + dims[0] * dims[1] * dims[2]
print('paper :', total_paper)
print('ribbon :', total_ribbon)
