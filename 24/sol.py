inp = [i.strip() for i in open('input').readlines()]

tiles = {}
for i in inp:
    nw, e = 0, 0
    j = 0
    while j < len(i):
        if i[j] == 'e' or i[j] == 'w':
            e = e+1 if i[j] == 'e' else e-1
        else:
            if i[j] == 'n':
                j += 1
                if i[j] == 'w':
                    nw += 1
                else:

                    # ne += 1
                    nw += 1
                    e += 1
            # 's'
            else:
                j += 1
                if i[j] == 'e':
                    # se = - nw
                    nw -= 1
                else:
                    # sw = - ne => ne -= 1
                    nw -= 1
                    e -= 1
        j += 1
    if (nw, e) not  in tiles:
        tiles[(nw, e)] = 0
    tiles[(nw, e)] += 1

print('Sol 1: ', sum([v % 2 for v in tiles.values()]))

# part 2

def find_neighbors(tile):
    (nw, e) = tile
    return [(nw, e+1), (nw, e-1), (nw+1, e), (nw-1, e), (nw-1, e-1), (nw+1, e+1)]

for i in range(1, 101):
    to_change = []
    # add neighbors first
    to_be_added = {}
    for tile in tiles:
        for neighbor in find_neighbors(tile):
            if neighbor not in to_be_added and neighbor not in tiles:
                to_be_added[neighbor] = 0
    for tile in to_be_added:
        if tile not in tiles:
            tiles[tile] = 0

    for tile in tiles:
        black_neighbors = sum([tiles[j] % 2 if j in tiles else 0 for j in find_neighbors(tile)])
        # white
        if tiles[tile] % 2 == 0 and black_neighbors == 2:
            to_change.append(tile)
        # black
        elif tiles[tile] % 2 == 1 and (black_neighbors == 0 or black_neighbors > 2):
            to_change.append(tile)
    for tile in to_change:
        tiles[tile] += 1

print('Sol 2: ', sum([v % 2 for v in tiles.values()]))
