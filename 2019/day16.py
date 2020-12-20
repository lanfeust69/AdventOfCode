file = open('test.in')

line = file.readline()[:-1]
# line = '02935109699940807407585447034323'
# line = '12345678'

data = [int(c) for c in line]
pattern = [0, 1, 0, -1]
offset = int(line[:7])
# the shortcut we use is only valid in second half of the input,
# where the i-th input pattern is i zeros followed by ones
assert offset > len(data) * 5000
long_data = data[offset % len(data):] + data * (10000 - offset // len(data) - 1)

for _ in range(100):
    new_data = []
    for i in range(len(data)):
        s = 0
        for j in range(len(data)):
            mult = (j + 1) % (len(pattern) * (i + 1)) // (i + 1)
            s += data[j] * pattern[mult]
        new_data.append(abs(s) % 10)
    data = new_data
    cumul = 0
    for i in range(len(long_data)):
        pos = len(long_data) - 1 - i
        cumul = (cumul + long_data[pos]) % 10
        long_data[pos] = cumul
    # print(''.join(map(str, data[-8:])))
    # print(data)

print(''.join(map(str, data[:8])))
print(''.join(map(str, long_data[:8])))
