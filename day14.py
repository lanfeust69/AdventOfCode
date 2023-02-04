target = 320851
target_arr = [int(d) for d in str(target)]
recipes = [3, 7]
p0, p1 = 0, 1
part2 = -1

while part2 == -1 or len(recipes) < target + 10:
    n = recipes[p0] + recipes[p1]
    if n > 9:
        recipes.append(n // 10)
        if part2 == -1 and all(target_arr[-i] == recipes[-i] for i in range(1, len(target_arr) + 1)):
            part2 = len(recipes) - len(target_arr)
    recipes.append(n % 10)
    if part2 == -1 and all(target_arr[-i] == recipes[-i] for i in range(1, len(target_arr) + 1)):
        part2 = len(recipes) - len(target_arr)
    p0 = (p0 + 1 + recipes[p0]) % len(recipes)
    p1 = (p1 + 1 + recipes[p1]) % len(recipes)

print(''.join(map(str, recipes[target:target + 10])))
print(part2)
