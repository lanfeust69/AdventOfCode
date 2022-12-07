score = 0

for line in open('test.in'):
    opp, me = line.split()
    opp = ord(opp) - ord('A')
    me = ord(me) - ord('X')
    # res = 3 if opp == me else 6 if me == (opp + 1) % 3 else 0
    # score += res + me + 1
    score += me * 3 + (opp + 3 + me - 1) % 3 + 1

print(score)
