for line in open('test.in'):
    s = line.rstrip()

res = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        res += int(s[i])
if s[0] == s[-1]:
    res += int(s[-1])

print(res)

res = 0
for i in range(len(s) // 2):
    if s[i] == s[i + len(s) // 2]:
        res += int(s[i]) * 2

print(res)
