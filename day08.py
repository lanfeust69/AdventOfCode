import math

lines = [line.rstrip() for line in open('test.in')]
moves = lines[0]
nb = len(moves)
graph = {}
for line in lines[2:]:
    node, children = line.split(' = (')
    graph[node] = children[:-1].split(', ')

cur = 'AAA'
pos = 0
while cur != 'ZZZ':
    cur = graph[cur][moves[pos % nb] == 'R']
    pos += 1

print(pos)

def path_len(node):
    cur = node
    seen = {}
    oks = []
    pos = 0
    while True:
        if (cur, pos % nb) in seen:
            return seen[(cur, pos % nb)], pos - seen[(cur, pos % nb)], oks
        seen[(cur, pos % nb)] = pos
        if cur[-1] == 'Z':
            oks.append(pos)
        cur = graph[cur][moves[pos % len(moves)] == 'R']
        pos += 1

lcm = 1
for node in graph:
    if node[-1] == 'A':
        cycle_start, cycle_len, oks = path_len(node)
        print(cycle_start, cycle_len, oks)
        if len(oks) != 1 or cycle_len != oks[0]:
            raise ValueError('does not match expectation that avoids needing chinese remainder')
        lcm = math.lcm(cycle_len, lcm)

print(lcm)
