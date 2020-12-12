import sys
sys.stdin = open('test.in')

nums = []
for line in sys.stdin:
    nums.append(int(line))

seen = {}
for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        seen[nums[i] + nums[j]] = (nums[i], nums[j])

for n in nums:
    if (2020 - n) in seen:
        a = seen[2020 - n][0]
        b = seen[2020 - n][1]
        print(f'{a} + {b} + {n} = {a + b + n}; {a} * {b} * {n} = {a * b * n}')
        break
