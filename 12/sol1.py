instr = [[i[0],int(i[1:].strip('\n'))] for i in open("input").readlines()]

L = 'L'
R = 'R'
F = 'F'

N = 'N'
W = 'W'
E = 'E'
S = 'S'

RIGHT = 'east'
LEFT = 'west'
DOWN = 'south'
UP = 'north'

right, up = 0, 0
face = RIGHT

def move(h, steps):
    global instr, right, up, face
    if h == L:
        if face == RIGHT:
            if steps == 90:
                face = UP
            elif steps == 180:
                face =LEFT
            else:
                face = DOWN
        elif face == UP:
            if steps == 90:
                face = LEFT
            elif steps == 180:
                face = DOWN
            else:
                face = RIGHT
        elif face == LEFT:
            if steps == 90:
                face = DOWN
            elif steps == 180:
                face = RIGHT
            else:
                face = UP
        elif face == DOWN:
            if steps == 90:
                face = RIGHT
            elif steps == 180:
                face = UP
            else:
                face = LEFT
    if h == R:
        if face == RIGHT:
            if steps == 90:
                face = DOWN
            elif steps == 180:
                face = LEFT
            else:
                face = UP
        elif face == DOWN:
            if steps == 90:
                face = LEFT
            elif steps == 180:
                face = UP
            else:
                face = RIGHT
        elif face == LEFT:
            if steps == 90:
                face = UP
            elif steps == 180:
                face = RIGHT
            else:
                face = DOWN
        elif face == UP:
            if steps == 90:
                face = RIGHT
            elif steps == 180:
                face = DOWN
            else:
                face = LEFT

    if h == F:
        if face == RIGHT:
            right += steps
        elif face == DOWN:
            up -= steps
        elif face == LEFT:
            right -= steps
        else:
            up += steps
    if h == N:
        up += steps
    if h == W:
        right -= steps
    if h == S:
        up -= steps
    if h == E:
        right += steps

def solve():
    global instr, right, up
    for i in instr:
        move(i[0], i[1])
    print(abs(right)+abs(up))

solve()
