lines = [line.rstrip() for line in open('test.in')]

res1 = ''
res2 = ''
for i in range(len(lines[0])):
    s = ''.join(line[i] for line in lines)
    freqs = [s.count(chr(ord('a') + l)) for l in range(26)]
    res1 += chr(ord('a') + freqs.index(max(freqs)))
    res2 += chr(ord('a') + freqs.index(min(f for f in freqs if f > 0)))

print(res1, res2)
