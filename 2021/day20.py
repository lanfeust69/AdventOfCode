image = []
for line in open('test.in'):
    if len(line) < 2:
        algo = ''.join(image)
        image = []
    else:
        image.append(line[:-1])

def sharpen(image, outside_light):
    h, w = len(image), len(image[0])
    new_image = [[' '] * (w + 2) for _ in range(h + 2)]
    for r in range(h + 2):
        for c in range(w + 2):
            index = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    is_light = outside_light
                    r_image, c_image = r + i - 1, c + j - 1
                    if r_image >= 0 and r_image < h and c_image >= 0 and c_image < w:
                        is_light = image[r_image][c_image] == '#'
                    index *= 2
                    if is_light:
                        index += 1
            new_image[r][c] = algo[index]
    return new_image, algo[-1 if outside_light else 0] == '#'

outside_light = False
for i in range(50):
    print('applying round', i)
    image, outside_light = sharpen(image, outside_light)

print(sum(c == '#' for line in image for c in line))
