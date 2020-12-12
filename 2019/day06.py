file = open('test.in')

graph = {}
for line in file:
    a, b = line[:-1].split(')')
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b not in graph:
        graph[b] = []

def count(n, depth):
    if n not in graph:
        return depth
    return depth + sum(count(moon, depth + 1) for moon in graph[n])

print(count('COM', 0))

def find_you_and_san(n):
    if n == 'YOU' or n == 'SAN':
        return {n: 0}
    res = {}
    for moon in graph[n]:
        res.update(find_you_and_san(moon))
    if 'FOUND' in res:
        return res
    if 'YOU' in res and 'SAN' in res:
        res['FOUND'] = res['YOU'] + res['SAN']
        return res
    for k in res:
        res[k] += 1
    return res

print(find_you_and_san('COM')['FOUND'])
