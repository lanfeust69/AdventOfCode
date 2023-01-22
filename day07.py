weights = {}
total_weights = {}
parents = {}
graph = {}

for line in open('test.in'):
    tokens = line.rstrip().split(' -> ')
    name, weight = tokens[0].split()
    weight = int(weight[1:-1])
    weights[name] = weight
    if len(tokens) > 1:
        children = tokens[1].split(', ')
        graph[name] = children
        for child in children:
            parents[child] = name

root = ''
for name in weights:
    if name not in parents:
        root = name
    if name not in graph:
        graph[name] = []
print(root)

def compute_total_weights(node):
    total_weight = weights[node] + sum(compute_total_weights(child) for child in graph[node])
    total_weights[node] = total_weight
    return total_weight
compute_total_weights(root)

def fix(node, delta):
    children = graph[node]
    if len(children) == 0:
        print('[suspicious] fix weight of', node, 'by', delta, 'to reach', weights[node] + delta)
        return
    if len(children) == 1:
        fix(children[0], delta)
        return
    nb_different = sum(total_weights[children[i]] != total_weights[children[0]] for i in range(1, len(children)))
    if nb_different == 0:
        print('[suspicious] fix weight of', node, 'by', delta, 'to reach', weights[node] + delta)
        return
    if len(children) != 2:
        raise ValueError('should already have been dealt with')
    w1, w2 = [total_weights[children[i]] for i in range(2)]
    if w1 == w2 + delta:
        print('fix weight of', children[1], 'by', delta, 'to reach', weights[children[1]] + delta)
    elif w2 == w1 + delta:
        print('fix weight of', children[0], 'by', delta, 'to reach', weights[children[0]] + delta)
    else:
        raise ValueError('more that one incorrect weight ?')

def check_balance(node):
    children = graph[node]
    subs = [check_balance(child) for child in children]
    if len(subs) == 0:
        return True
    if len(subs) == 1:
        return subs[0]
    for i in range(len(subs)):
        if not subs[i]:
            delta = total_weights[children[0 if i != 0 else 1]] - total_weights[children[i]]
            fix(children[i], delta)
            return True
    # all children balanced, check weights
    nb_different = sum(total_weights[children[i]] != total_weights[children[0]] for i in range(1, len(subs)))
    if nb_different == 0:
        return True
    if len(subs) == 2:
        # no way to choose which is incorrect at that point
        return False
    ko_child = 0 if nb_different > 1 else next(i for i in range(1, len(subs)) if total_weights[children[i]] != total_weights[children[0]])
    delta = total_weights[children[0 if ko_child != 0 else 1]] - total_weights[children[ko_child]]
    print('fix weight of', children[ko_child], 'by', delta, 'to reach', weights[children[ko_child]] + delta)
    weights[children[ko_child]] += delta
    compute_total_weights(root)
    return True

check_balance(root)
