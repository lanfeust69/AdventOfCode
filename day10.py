import sys
sys.stdin = open('test.in')

nums = [int(l) for l in sys.stdin.readlines()]
nums.sort()

diffs = [0, 0, 0, 1]
diffs[nums[0]] += 1

for i in range(1, len(nums)):
    diffs[nums[i] - nums[i - 1]] += 1

print(diffs)
print(diffs[1] * diffs[3])

nb_ways = [0] * (nums[-1] + 4)
nb_ways[-1] = 1
for n in reversed(nums):
    nb_ways[n] = sum(nb_ways[n + 1:n + 4])

print(sum(nb_ways[1:4]))
