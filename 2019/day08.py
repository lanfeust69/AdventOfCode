image = open('test.in').readline()[:-1]

nb_layer = len(image) // (25 * 6)
best_layer = ''
best_layer_val = 1000
for i in range(nb_layer):
    layer = image[25 * 6 * i:25 * 6 * (i + 1)]
    nb_zero = sum(1 for c in layer if c == '0')
    if nb_zero < best_layer_val:
        best_layer_val = nb_zero
        best_layer = layer

print(sum(1 for c in best_layer if c == '1') * sum(1 for c in best_layer if c == '2'))

for r in range(6):
    line = ''
    for c in range(25):
        color = '?'
        for i in range(nb_layer):
            ch = image[i * 25 * 6 + r * 25 + c]
            if ch == '2':
                continue
            color = ' ' if ch == '0' else '#'
            break
        line += color
    print(line)
