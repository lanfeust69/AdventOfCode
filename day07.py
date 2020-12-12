import sys, re
sys.stdin = open('test.in')

descriptions = {}
for line in sys.stdin:
    m = re.match(r'(.*) bags contain (.*)\.', line)
    if not m:
        continue
    contain = []
    for b in m.group(2).split(', '):
        m1 = re.match(r'(\d+) (.*) bags?', b)
        if m1:
            contain.append((int(m1.group(1)), m1.group(2)))
    descriptions[m.group(1)] = contain

cache = {}
def nb_for(bag):
    global cache
    if bag in cache:
        return cache[bag]
    s = 1  # the bag itself
    for nb, c in descriptions[bag]:
        s += nb * nb_for(c)
    cache[bag] = s
    return s

print(nb_for('shiny gold') - 1)  # we want what's inside, not counting the bag itself here
