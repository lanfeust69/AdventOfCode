row, col = 2978, 3083

seed, mult, mod = 20151125, 252533, 33554393

row, col = row - 1, col - 1 # 0-indexed !

nth = (row + col) * (row + col + 1) // 2 + col

print(pow(mult, nth, mod) * seed % mod)
