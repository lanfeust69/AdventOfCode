nums = [eval(line) for line in open('test.in')]

def explode(n, depth):
    if isinstance(n, list) and depth == 4:
        return True, n
    if isinstance(n[0], list):
        exploded, res = explode(n[0], depth + 1)
        if exploded:
            if isinstance(n[1], int):
                n[1] += res[1]
            else:
                to_add = n[1]
                while isinstance(to_add[0], list):
                    to_add = to_add[0]
                to_add[0] += res[1]
            if depth == 3:
                n[0] = 0
            return True, [res[0], 0]
    if isinstance(n[1], list):
        exploded, res = explode(n[1], depth + 1)
        if exploded:
            if isinstance(n[0], int):
                n[0] += res[0]
            else:
                to_add = n[0]
                while isinstance(to_add[1], list):
                    to_add = to_add[1]
                to_add[1] += res[0]
            if depth == 3:
                n[1] = 0
            return True, [0, res[1]]
    return False, None

def split(n):
    if isinstance(n, int):
        if n >= 10:
            return True, [n // 2, n - n // 2]
        else:
            return False, None
    splitted, res = split(n[0])
    if splitted:
        n[0] = res
        return True, n
    splitted, res = split(n[1])
    if splitted:
        n[1] = res
        return True, n
    return False, None

def reduce(n):
    exploded = True
    while exploded:
        exploded, _ = explode(n, 0)
    splitted, _ = split(n)
    if splitted:
        reduce(n)

def magnitude(n):
    if isinstance(n, int):
        return n
    return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

def clone(n):
    if isinstance(n, int):
        return n
    return [clone(n[0]), clone(n[1])]

# res = nums[0]
# for i in range(1, len(nums)):
#     res = [res, nums[i]]
#     reduce(res)

# print(magnitude(res))

best = 0
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        s = clone([nums[i], nums[j]])
        reduce(s)
        best = max(best, magnitude(s))
        s = clone([nums[j], nums[i]])
        reduce(s)
        best = max(best, magnitude(s))

print(best)
