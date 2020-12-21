import copy
import collections
import numpy as np
from sol1 import solve

tiles = [i.strip() for i in open('input').read().split('\n\n')]
ids = [i.split('\n')[0].split(' ')[1].strip(' :') for i in tiles]

adj_edges = solve()

ordered_tiles = []
ordered_ids = []
# first the corners
for idx in range(len(tiles)):
    if adj_edges[ids[idx]] == 2:
        ordered_tiles.append(tiles[idx])

for idx in range(len(tiles)):
    if adj_edges[ids[idx]] in [3, 4]:
        ordered_tiles.append(tiles[idx])

tiles = ordered_tiles

ids = [i.split('\n')[0].split(' ')[1].strip(' :') for i in tiles]
ups = [i.split('\n')[1].strip() for i in tiles]
downs = [i.split('\n')[-1].strip() for i in tiles]
lefts = ["".join([j[0] for j in i.split('\n')[1:]]) for i in tiles]
rights = ["".join([j[-1] for j in i.split('\n')[1:]]) for i in tiles]

tiles_d = {}
for t in tiles:
    tile = t.split(':')
    tiles_d[tile[0].split(' ')[1]] = [i for i in tile[1].lstrip('\n').split('\n')]

# left rotate
def rotate_90(tile):
    new_tile = []
    for i in range(len(tile[0])):
        new_entry = []
        for j in tile:
            new_entry.append(j[-1-i])
        new_tile.append("".join(new_entry))
    return new_tile

def mirror(tile):
    new_tile = []
    for i in tile:
        new_tile.append(i[::-1])
    return new_tile

def flip_down_up(tile):
    new_tile = []
    for i in range(len(tile)):
        new_tile.append(tile[len(tile) -1 -i])
    return new_tile

def jigsaw_falling_into_place(tiles_d, ids, ups, downs, lefts, rights):
    new_tiles_d = copy.deepcopy(tiles_d)
    new_ids = copy.deepcopy(ids)
    new_ups = copy.deepcopy(ups)
    new_downs = copy.deepcopy(downs)
    new_lefts = copy.deepcopy(lefts)
    new_rights = copy.deepcopy(rights)
    collected = {}
    prev_len = 0
    while len(new_ids) > 1:
        if prev_len == len(new_ids):
            break
        prev_len = len(new_ids)
        tiles_d.clear()
        ids.clear()
        ups.clear()
        downs.clear()
        lefts.clear()
        rights.clear()

        tiles_d = copy.deepcopy(new_tiles_d)
        ids = copy.deepcopy(new_ids)
        ups = copy.deepcopy(new_ups)
        downs = copy.deepcopy(new_downs)
        lefts = copy.deepcopy(new_lefts)
        rights = copy.deepcopy(new_rights)

        new_tiles_d.clear()
        new_ids.clear()
        new_ups.clear()
        new_downs.clear()
        new_lefts.clear()
        new_rights.clear()

        collected.clear()

        for tile in range(len(ids)):

            if ids[tile] in collected.keys():
                continue

            for idx in range(len(ids)):
                new_tile = []
                if ids[tile] in collected.keys():
                    break
                if ids[idx] in collected.keys() or idx == tile:
                    continue

                if ups[tile] == ups[idx]:
                    new_tile = flip_down_up(tiles_d[ids[tile]])
                    new_tile.extend(tiles_d[ids[idx]])

                elif ups[tile] == downs[idx]:
                    new_tile = flip_down_up(tiles_d[ids[tile]])
                    new_tile.extend(flip_down_up(tiles_d[ids[idx]]))

                elif ups[tile] == lefts[idx]:
                    new_tile = flip_down_up(tiles_d[ids[tile]])
                    rot_idx = flip_down_up(rotate_90(tiles_d[ids[idx]]))
                    new_tile.extend(rot_idx)

                elif ups[tile] == rights[idx]:
                    new_tile = flip_down_up(tiles_d[ids[tile]])
                    rot_idx = rotate_90(tiles_d[ids[idx]])
                    new_tile.extend(rot_idx)

                elif ups[tile][::-1] == ups[idx]:
                    new_tile = flip_down_up(mirror(tiles_d[ids[tile]]))
                    new_tile.extend(tiles_d[ids[idx]])

                elif ups[tile][::-1] == downs[idx]:
                    new_tile = flip_down_up(mirror(tiles_d[ids[tile]]))
                    new_tile.extend(flip_down_up(tiles_d[ids[idx]]))

                elif ups[tile][::-1] == lefts[idx]:
                    new_tile = flip_down_up(mirror(tiles_d[ids[tile]]))
                    rot_idx = flip_down_up(rotate_90(tiles_d[ids[idx]]))
                    new_tile.extend(rot_idx)

                elif ups[tile][::-1] == rights[idx]:
                    new_tile = flip_down_up(mirror(tiles_d[ids[tile]]))
                    rot_idx = rotate_90(tiles_d[ids[idx]])
                    new_tile.extend(rot_idx)


                elif downs[tile] == downs[idx]:
                    new_tile = tiles_d[ids[tile]]
                    new_tile.extend(flip_down_up(tiles_d[ids[idx]]))

                elif downs[tile] == ups[idx]:
                    new_tile = tiles_d[ids[tile]]
                    new_tile.extend(tiles_d[ids[idx]])

                elif downs[tile] == lefts[idx]:
                    new_tile = tiles_d[ids[tile]]
                    rot_idx = flip_down_up(rotate_90(tiles_d[ids[idx]]))
                    new_tile.extend(rot_idx)

                elif downs[tile] == rights[idx]:
                    new_tile = tiles_d[ids[tile]]
                    new_tile.extend(rotate_90(tiles_d[ids[idx]]))

                elif downs[tile][::-1] == downs[idx]:
                    new_tile = mirror(tiles_d[ids[tile]])
                    new_tile.extend(flip_down_up(tiles_d[ids[idx]]))

                elif downs[tile][::-1] == ups[idx]:
                    new_tile = mirror(tiles_d[ids[tile]])
                    new_tile.extend(tiles_d[ids[idx]])

                elif downs[tile][::-1] == lefts[idx]:
                    new_tile = mirror(tiles_d[ids[tile]])
                    rot_idx = flip_down_up(rotate_90(tiles_d[ids[idx]]))
                    new_tile.extend(rot_idx)

                elif downs[tile][::-1] == rights[idx]:
                    new_tile = mirror(tiles_d[ids[tile]])
                    new_tile.extend(rotate_90(tiles_d[ids[idx]]))

                elif lefts[tile] == lefts[idx]:
                    new_tile = rotate_90(tiles_d[ids[tile]])
                    rot_idx = flip_down_up(rotate_90(tiles_d[ids[idx]]))
                    new_tile.extend(rot_idx)

                elif lefts[tile] == rights[idx]:
                    new_tile = rotate_90(tiles_d[ids[tile]])
                    rot_idx = rotate_90(tiles_d[ids[idx]])
                    new_tile.extend(rot_idx)

                elif lefts[tile] == ups[idx]:
                    new_tile = rotate_90(tiles_d[ids[tile]])
                    new_tile.extend(tiles_d[ids[idx]])

                elif lefts[tile] == downs[idx]:
                    new_tile = rotate_90(tiles_d[ids[tile]])
                    rot_idx = flip_down_up(tiles_d[ids[idx]])
                    new_tile.extend(rot_idx)

                elif lefts[tile][::-1] == lefts[idx]:
                    new_tile = mirror(rotate_90(tiles_d[ids[tile]]))
                    rot_idx = flip_down_up(rotate_90(tiles_d[ids[idx]]))
                    new_tile.extend(rot_idx)

                elif lefts[tile][::-1] == rights[idx]:
                    new_tile = mirror(rotate_90(tiles_d[ids[tile]]))
                    rot_idx = rotate_90(tiles_d[ids[idx]])
                    new_tile.extend(rot_idx)

                elif lefts[tile][::-1] == ups[idx]:
                    new_tile = mirror(rotate_90(tiles_d[ids[tile]]))
                    new_tile.extend(tiles_d[ids[idx]])

                elif lefts[tile][::-1] == downs[idx]:
                    new_tile = mirror(rotate_90(tiles_d[ids[tile]]))
                    rot_idx = flip_down_up(tiles_d[ids[idx]])
                    new_tile.extend(rot_idx)

                elif rights[tile] == ups[idx]:
                    new_tile = flip_down_up(rotate_90(tiles_d[ids[tile]]))
                    new_tile.extend(tiles_d[ids[idx]])

                elif rights[tile] == downs[idx]:
                    new_tile = flip_down_up(rotate_90(tiles_d[ids[tile]]))
                    new_tile.extend(flip_down_up(tiles_d[ids[idx]]))

                elif rights[tile] == lefts[idx]:
                    new_tile = flip_down_up(rotate_90(tiles_d[ids[tile]]))
                    rot_idx = flip_down_up(rotate_90(tiles_d[ids[idx]]))
                    new_tile.extend(rot_idx)

                elif rights[tile] == rights[idx]:
                    new_tile = flip_down_up(rotate_90(tiles_d[ids[tile]]))
                    rot_idx = rotate_90(tiles_d[ids[idx]])
                    new_tile.extend(rot_idx)

                elif rights[tile][::-1] == ups[idx]:
                    new_tile = flip_down_up(mirror(rotate_90(tiles_d[ids[tile]])))
                    new_tile.extend(tiles_d[ids[idx]])

                elif rights[tile][::-1] == downs[idx]:
                    new_tile = flip_down_up(mirror(rotate_90(tiles_d[ids[tile]])))
                    new_tile.extend(flip_down_up(tiles_d[ids[idx]]))

                elif rights[tile][::-1] == lefts[idx]:
                    new_tile = flip_down_up(mirror(rotate_90(tiles_d[ids[tile]])))
                    rot_idx = flip_down_up(rotate_90(tiles_d[ids[idx]]))
                    new_tile.extend(rot_idx)

                elif rights[tile][::-1] == rights[idx]:
                    new_tile = flip_down_up(mirror(rotate_90(tiles_d[ids[tile]])))
                    rot_idx = rotate_90(tiles_d[ids[idx]])
                    new_tile.extend(rot_idx)

                # check if part of


                if len(new_tile) > 0:
                    collected[ids[tile]] = 0
                    collected[ids[idx]] = 0
                    new_ups.append(new_tile[0])
                    new_downs.append(new_tile[-1])
                    new_lefts.append("".join([j[0] for j in new_tile]))
                    new_rights.append("".join([j[-1] for j in new_tile]))
                    new_ids.append("".join([ids[tile],' ',ids[idx]]))
                    new_tiles_d[new_ids[-1]] = new_tile
            if ids[tile] not in collected:
                collected[ids[tile]] = 0
                new_tile = copy.deepcopy(tiles_d[ids[tile]])
                new_ups.append(ups[tile])
                new_downs.append(downs[tile])
                new_lefts.append(lefts[tile])
                new_rights.append(rights[tile])
                new_ids.append(ids[tile])
                new_tiles_d[new_ids[-1]] = new_tile

    return(new_tiles_d)

# just one big tile returned - the whole image
new_tiles_d = jigsaw_falling_into_place(tiles_d, ids, ups, downs, lefts, rights)
print(len(new_tiles_d))

for key in new_tiles_d:
    picture = []
    for i in new_tiles_d[key]:
        picture.append(i)

borders = {0: 0, len(picture)-1: 0}
for i in range(1, len(picture)):
    if picture[i-1] == picture[i]:
        borders[i-1] = 0
        borders[i] = 0

# remove border lines
no_borders_picture = []
for i in range(len(picture)):
    if i not in borders:
        no_borders_picture.append(picture[i])

# remove border columns
picture.clear()
picture = rotate_90(no_borders_picture)
no_borders_picture.clear()
for i in range(len(picture)):
    if i not in borders:
        no_borders_picture.append(picture[i])

total_hashtags_count = 0
for i in no_borders_picture:
    total_hashtags_count += i.count('#')

## let's find the monsters

'''
                  #
#    ##    ##    ###
 #  #  #  #  #  #
'''
MONSTER_FLESH = 15

monster = []
monster.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0])
monster.append([1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1])
monster.append([0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0])

p = no_borders_picture
possible_pictures = [ p, rotate_90(p), flip_down_up(p), flip_down_up(rotate_90(p)), mirror(p), mirror(flip_down_up(p)), mirror(rotate_90(p)), mirror(flip_down_up(rotate_90(p))), rotate_90(mirror(p)), flip_down_up(mirror(p)), flip_down_up(rotate_90(mirror(p))), rotate_90(mirror(p)), flip_down_up(mirror(p)), flip_down_up(rotate_90(mirror(p)))]

monsters_cnt = 0
for pict in possible_pictures:
    if monsters_cnt > 0:
        break

    picture = []
    for i in pict:
        boolean_line = []
        for j in i:
            if j == '#':
                boolean_line.append(1)
            else:
                boolean_line.append(0)
        picture.append(boolean_line)

    i, j = 0, 0
    while True:
        res = [np.logical_and(monster[k], picture[i+k][j:j+len(monster[k])]) for k in [0,1,2]]
        matched = sum([sum(r) for r in res])
        if matched == MONSTER_FLESH:
            monsters_cnt += 1
        if j+1+len(monster[0]) < len(picture[i]):
            j += 1
        elif i+len(monster) < len(picture):
            i += 1
            j = 0
        else:
            break

print("Monsters found: ", monsters_cnt)
print("Total '#' in picture: ", total_hashtags_count)
print("Sol 2: ", total_hashtags_count - MONSTER_FLESH * monsters_cnt)
