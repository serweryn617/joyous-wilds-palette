COLORS = (
    {'name': 'green', 'base': (0, 204, 82), 'count': 6, 'delta': (0, -25, -10)},
    {'name': 'pink', 'base': (216, 73, 255), 'count': 6, 'delta': (-22, -11, -25)},

    {'name': 'white', 'base': (255, 255, 255), 'count': 1},
    {'name': 'text', 'base': (204, 204, 204), 'count': 1},
    {'name': 'light_gray', 'base': (140, 140, 140), 'count': 1},
    {'name': 'dark_gray', 'base': (100, 100, 100), 'count': 1},
    {'name': 'bg_light', 'base': (31, 31, 31), 'count': 1},
    {'name': 'bg_dark', 'base': (24, 24, 24), 'count': 1},
)

print('GIMP Palette')
print('Name: Joyous Wilds')
print('Columns: 6')
print('# Joyous Wilds Palette')
print('# Color palette for creating complementary green and pink themes with dark backgrounds.')
print('# https://github.com/serweryn617/joyous-wilds-palette')

for color in COLORS:
    r, g, b = color['base']

    if color['count'] == 1:
        print(f'{r:3d} {g:3d} {b:3d}', color['name'])
        continue

    for i in range(color['count']):
        nr, ng, nb = r + i * color['delta'][0], g + i * color['delta'][1], b + i * color['delta'][2]
        print(f'{nr:3d} {ng:3d} {nb:3d}', color['name'] + str(i + 1))
