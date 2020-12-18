import copy

inp = []
for i in open('input').readlines():
    i = i.strip()
    inp.append([1 if j == '#' else 0 for j in i])

def create_z(lj, lx):
    z = []
    for x in range(0, lx):
        z.append([])
        for j in range(0, lj):
            z[x].append(0)
    return z

def update_existing_grid(g):
    for i in range(len(g)):
        tmp = [0] + g[i]
        tmp.append(0)
        g[i] = copy.deepcopy(tmp)
    tempx = [[]]
    for i in range(len(g[0])):
        tempx[0].append(0)
    tmp = copy.deepcopy(tempx)
    tmp = tmp + g
    tempx = []
    for i in range(len(g[0])):
        tempx.append(0)
    tmp.append(tempx)
    g = copy.deepcopy(tmp)
    return g

inp = update_existing_grid(inp)
new_z = create_z(len(inp[0]),len(inp))
grid = [create_z(len(inp[0]),len(inp)), inp, create_z(len(inp[0]),len(inp))]

def update_grid(grid):
    new_grid = []
    for g in range(len(grid)):
        new_grid.append(copy.deepcopy(update_existing_grid(grid[g])))
    new_z = create_z(len(new_grid[0][0]), len(new_grid[0]))
    new_z1 = copy.deepcopy(new_z)
    new_grid = [new_z1] + new_grid
    new_grid.append(new_z)
    return new_grid

def count_neighbors(z, x, j, grid):
    count = 0
    zl = z-1 if z > 0 else 0
    xl = x-1 if x > 0 else 0
    jl = j-1 if j > 0 else 0
    zr = z+2 if z+2 < len(grid) else len(grid)
    xr = x+2 if x+2 < len(grid[0]) else len(grid[0])
    jr = j+2 if j+2 < len(grid[0][0]) else len(grid[0][0])
    for zi in range(zl, zr):
        for xi in range(xl, xr):
            for ji in range(jl, jr):
                count += grid[zi][xi][ji]
    return count

for i in range(0,6):
    new_grid = copy.deepcopy(grid)
    for z in range(len(grid)):
        for x in range(len(grid[z])):
            for j in range(len(grid[z][x])):
                state = grid[z][x][j]
                ln = count_neighbors(z, x, j, grid)
                if (state and (not 3 <= ln <= 4)):
                    new_grid[z][x][j] = 0
                elif (state == 0 and ln == 3):
                    new_grid[z][x][j] = 1
    grid = copy.deepcopy(new_grid)
    temp = update_grid(grid)
    grid = copy.deepcopy(temp)

count = 0
for z in range(len(grid)):
    for x in range(len(grid[z])):
        for j in range(len(grid[z][x])):
            count += grid[z][x][j]
print('Sol: ', count)
