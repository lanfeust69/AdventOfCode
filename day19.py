n = 3018458

first, p, nb = 0, 1, n

while nb > 1:
    first, p, nb = first + (nb % 2) * 2**p, p + 1, nb // 2

print(first + 1)

# basic simul
# players = list(range(n))
# while len(players) > 1:
#     to_remove = len(players) // 2
#     players = players[1:to_remove] + players[to_remove + 1:] + [players[0]]
# print(players[0] + 1)

used = [False] * n
succ = [(i + 1) % n for i in range(n)]
def find_succ(x):
    if not used[succ[x]]:
        return succ[x]
    res = find_succ(succ[x])
    succ[x] = res
    return res

cur, opp, remain = 0, n // 2, n
while remain > 1:
    used[opp] = True
    cur = find_succ(cur)
    opp = find_succ(opp)
    if remain % 2:
        opp = find_succ(opp)
    remain -= 1

print(cur + 1)
