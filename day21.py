import re

lines = []
for line in open('test.in'):
    m = re.match(r'(.*) \(contains (.*)\)', line)
    if m:
        lines.append((set(m.group(1).split()), set(m.group(2).split(', '))))

all_ingredients = set()
all_allergens = set()
nb_seen = {}
for ings, als in lines:
    all_ingredients.update(ings)
    for ing in ings:
        nb_seen[ing] = nb_seen.get(ing, 0) + 1
    all_allergens.update(als)

per_allergen = {al: set(all_ingredients) for al in all_allergens}
found = {}
harmful = set()

progress = True
while progress:
    progress = False
    for al in all_allergens:
        s = per_allergen[al]
        count = len(s)
        for line in lines:
            if al in line[1]:
                s.intersection_update(line[0])
        if len(s) < count:
            progress = True
        if len(s) == 1:
            ing = min(s)
            harmful.add(ing)
            found[al] = min(s)
            for line in lines:
                if ing in line[0]:
                    line[0].remove(ing)
                if al in line[1]:
                    line[1].remove(al)
    all_allergens.difference_update(found)

assert len(all_allergens) == 0

print(sum(nb_seen[ing] for ing in all_ingredients.difference(harmful)))
print(','.join(found[al] for al in sorted(found)))
