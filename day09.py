import sys
sys.stdin = open('test.in')

nums = [int(l) for l in sys.stdin.readlines()]
window = 25

reachable = {}
for i in range(window - 1):
    for j in range(i + 1, window):
        s = nums[i] + nums[j]
        if s in reachable:
            reachable[s].append((i, j))
        else:
            reachable[s] = [(i, j)]

target = 0
for i in range(window, len(nums)):
    cur = nums[i]
    if cur not in reachable:
        target = cur
        break
    to_remove = nums[i - window]
    for j in range(i - window + 1, i):
        s = to_remove + nums[j]
        new_pairs = [p for p in reachable[s] if p[0] != i - window]
        if len(new_pairs) == 0:
            del reachable[s]
        else:
            reachable[s] = new_pairs
        s = nums[i] + nums[j]
        if s in reachable:
            reachable[s].append((j, i))
        else:
            reachable[s] = [(j, i)]

print(target)

start, end, sum = 0, 0, 0
while end < len(nums):
    while sum < target:
        sum += nums[end]
        end += 1
    while sum > target:
        sum -= nums[start]
        start += 1
    if sum == target:
        print(min(nums[i] for i in range(start, end)) + max(nums[i] for i in range(start, end)))
        break

