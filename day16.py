import re

file = open('test.in')
in_rules = True
in_my_ticket = True
rules = {}
my_ticket = None
nearby_tickets = []
for line in file:
    if in_rules:
        if re.match(r'your ticket:', line):
            in_rules = False
            continue
        m = re.match(r'(.*): (.*)', line[:-1])
        if m:
            rule_name = m.group(1)
            rules[rule_name] = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in m.group(2).split(' or ')]
    else:
        ticket = line.split(',')
        if len(ticket) != len(rules):
            continue
        ticket = list(map(int, ticket))
        if in_my_ticket:
            my_ticket = ticket
            in_my_ticket = False
        else:
            nearby_tickets.append(ticket)

def match_rule(rule, val):
    return any(interval[0] <= val <= interval[1] for interval in rule)

res = 0
valid_tickets = []
for ticket in nearby_tickets:
    is_valid = True
    for val in ticket:
        if any(match_rule(rule, val) for _, rule in rules.items()):
            continue
        res += val
        is_valid = False
    if is_valid:
        valid_tickets.append(ticket)

possible = {}
for rule_name, ranges in rules.items():
    poss = set()
    for i in range(len(rules)):
        is_possible = True
        for ticket in valid_tickets:
            if not match_rule(ranges, ticket[i]):
                is_possible = False
                break
        if is_possible:
            poss.add(i)
    possible[rule_name] = poss

done = False
progress = True
while progress and not done:
    done = True
    progress = False
    for rule_name in rules:
        if len(possible[rule_name]) != 1:
            done = False
            continue
        else:
            assigned = next(iter(possible[rule_name]))
            for other in rules:
                if other == rule_name:
                    continue
                if assigned in possible[other]:
                    progress = True
                    possible[other].remove(assigned)

res = 1
for rule_name in rules:
    if rule_name.startswith('departure'):
        res *= my_ticket[next(iter(possible[rule_name]))]

print(res)
