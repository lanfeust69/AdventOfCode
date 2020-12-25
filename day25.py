# a = 5764801
# b = 17807724
a = 14205034
b = 18047856
mod = 20201227
seed = 7
res = 1

n = 1
while True:
    if n == a:
        print(res)
        break
    n = n * seed % mod
    res = res * b % mod
