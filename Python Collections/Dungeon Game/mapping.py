TILES = ('-', ' ', '-', ' ', '-', '||',
         '_', '|', '_', '|', '_', '|', '||',
         '&', ' ', '_', ' ', '||',
         ' ', ' ', ' ', '^', ' ', '||'
)

for tile in TILES:
    if tile == '||':
        output = ""
        line_end = "\n"
    else:
        output = tile
        line_end = ""
    print(output, end = line_end)
