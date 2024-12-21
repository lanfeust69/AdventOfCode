from functools import cache

# codes = ['029A', '980A', '179A', '456A', '379A']
codes = ['540A', '985A', '463A', '671A', '382A']

keypad = ['789', '456', '123', '#0A']
keypad_pos = {keypad[r][c]: (r, c) for c in range(3) for r in range(4)}
controlpad = ['#^A', '<v>']
controlpad_pos = {controlpad[r][c]: (r, c) for c in range(3) for r in range(2)}

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
dir_names = '><v^'

@cache
def pad_moves(cur, dest, is_keypad):
    pad_pos = keypad_pos if is_keypad else controlpad_pos
    pad = keypad if is_keypad else controlpad
    rs, cs = pad_pos[cur]
    re, ce = pad_pos[dest]
    reachable = {(rs, cs): ['']}
    while (re, ce) not in reachable:
        new_reachable = {}
        for (r, c), paths in reachable.items():
            for d in range(4):
                rr, cc = r + dirs[d][0], c + dirs[d][1]
                if 0 <= rr < len(pad) and 0 <= cc < 3 and pad[rr][cc] != '#':
                    if (rr, cc) not in new_reachable:
                        new_reachable[(rr, cc)] = []
                    for path in paths:
                        new_reachable[(rr, cc)].append(path + dir_names[d])
        reachable = new_reachable
    return [path + 'A' for path in reachable[(re, ce)]]

@cache
def nb_control_moves(cur, dest, depth):
    if depth == 0:
        return len(pad_moves(cur, dest, False)[0])
    res = -1
    for path in pad_moves(cur, dest, False):
        candidate = sum(nb_control_moves(path[i - 1] if i > 0 else 'A', path[i], depth - 1) for i in range(len(path)))
        if res == -1 or candidate < res:
            res = candidate
    return res

def solve(code, depth):
    cur = 'A'
    res = 0
    for c in code:
        best = -1
        for path in pad_moves(cur, c, True):
            candidate = sum(nb_control_moves(path[i - 1] if i > 0 else 'A', path[i], depth - 1) for i in range(len(path)))
            if best == -1 or candidate < best:
                best = candidate
        res += best
        cur = c
    return res

print(sum(solve(code, 2) * int(code[:-1]) for code in codes))
print(sum(solve(code, 25) * int(code[:-1]) for code in codes))
