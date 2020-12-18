import copy

inp = []
for i in open('input').readlines():
    i = i.strip()
    inp.append([1 if j == '#' else 0 for j in i])

mapd = {}
for i in range(len(inp)):
    for j in range(len(inp[i])):
        w, z = 0, 0
        if inp[i][j]:
           mapd[(w, z, i,j)] = 1
max_w, max_z = 0, 0
max_x = len(inp)
max_j = len(inp[0])
min_w, min_z, min_x, min_j = 0, 0, 0, 0

def count_neighbors(w, z, x, j):
    global mapd
    count = 0
    for wi in range(w-1, w+2):
        for zi in range(z-1, z+2):
            for xi in range(x-1, x+2):
                for ji in range(j-1, j+2):
                    if (wi, zi, xi, ji) in mapd:
                        count += 1
    return count

for i in range(6):
    new_map = {}
    for w in range(min_w-1, max_w + 2):
        for z in range(min_z-1, max_z + 2):
            for x in range(min_x-1, max_x + 2):
                for j in range(min_j-1, max_j + 2):
                    state = (w, z, x, j) in mapd
                    ln = count_neighbors(w, z, x, j)
                    if (state and ln in [3,4]) or (state == 0 and ln == 3):
                        new_map[(w, z, x, j)] = 1
                        max_w = w if w > max_w else max_w
                        max_z = z if z > max_z else max_z
                        max_x = x if x > max_x else max_x
                        max_j = j if j > max_j else max_j
                        min_w = w if w < min_w else min_w
                        min_z = z if z < min_z else min_z
                        min_x = x if x < min_x else min_x
                        min_j = j if j < min_j else min_j
    mapd = new_map

print(len(mapd.keys()))
