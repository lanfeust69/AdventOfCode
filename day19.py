import re

file = open('test.in')

rules = {}
words = []
for line in file:
    p = line.split(':')
    if len(p) == 2:
        m = re.match(r' "(\w+)"', p[1])
        if m:
            rules[int(p[0])] = [[m.group(1)]]
        else:
            rules[int(p[0])] = [list(map(int, x.split())) for x in p[1].split('|')]
    elif len(line) > 1:
        words.append(line[:-1])

def matches_seq(s, offset, seq):
    if seq == []:
        return set([0])
    p = seq[0]
    if p not in rules:
        if s[offset:].startswith(p):
            return set(used + len(p) for used in matches_seq(s, offset + len(p), seq[1:]))
        else:
            return set()
    else:
        res = set()
        for used in matches_rule(s, offset, rules[p]):
            res.update(x + used for x in matches_seq(s, offset + used, seq[1:]))
        return res

def matches_rule(s, offset, rule):
    res = set()
    for seq in rule:
        res.update(matches_seq(s, offset, seq))
    return res

nb_ok = 0
for word in words:
    if len(word) in matches_rule(word, 0, rules[0]):
        nb_ok += 1

print(nb_ok)
