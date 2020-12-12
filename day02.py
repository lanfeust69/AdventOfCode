import sys, re
sys.stdin = open('test.in')

res0, res1 = 0, 0
for line in sys.stdin:
    match = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
    inf, sup, c, pwd = int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)
    count = sum(1 for cc in pwd if cc == c)
    if inf <= count <= sup:
        res0 += 1
    if len(pwd) >= sup and (pwd[inf - 1] == c or pwd[sup - 1] == c) and not (pwd[inf - 1] == c and pwd[sup - 1] == c):
        res1 += 1

print(res1)
