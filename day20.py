nums = [int(line.rstrip()) * 811589153 for line in open('test.in')]
n = len(nums)

res = list(range(n))
for _ in range(10):
    for i in range(n):
        if nums[i] == 0:
            continue
        j = res.index(i)
        dest = (j + nums[i]) % (n - 1)
        if dest == 0:
            dest = n - 1
        if dest < j:
            res = res[:dest] + [i] + res[dest:j] + res[j + 1:]
        else:
            res = res[:j] + res[j + 1:dest + 1] + [i] + res[dest + 1:]

# print(list(nums[i] for i in res))

z = nums.index(0)
z = res.index(z, 0)
print(sum(nums[res[(z + i * 1000) % n]] for i in range(1, 4)))
