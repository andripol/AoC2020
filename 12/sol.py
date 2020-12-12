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



def move2(h, steps):
    global instr, right, up, wp
    if (h == L or h == R) and steps == 180:
        wp[1] = -wp[1]
        wp[0] = -wp[0]
    if h == L and steps == 270:
        h = R
        steps = 90
    if h == R and steps == 270:
        h = L
        steps = 90

    if h == L and steps == 90:
        if wp[0]*wp[1] == 0:
            if wp[0] == 0 :
                wp[0] = -wp[1]
                wp[1] = 0
            else:
                wp[1] = wp[0]
                wp[0] = 0
        elif wp[0]*wp[1] > 0:
            temp = wp[1]
            wp[1] = wp[0]
            wp[0] = -temp
        else:
            temp = wp[1]
            wp[1] = wp[0]
            wp[0] = -temp
    if h == R and steps == 90:
        if wp[0]*wp[1] == 0:
            if wp[0] == 0 :
                wp[0] = wp[1]
                wp[1] = 0
            else:
                wp[1] = -wp[0]
                wp[0] = 0
        elif wp[0]*wp[1] > 0:
            temp = wp[1]
            wp[1] = -wp[0]
            wp[0] = temp
        else:
            temp = wp[1]
            wp[1] = -wp[0]
            wp[0] = temp

    # move ship
    if h == F:
        right += wp[0]*steps
        up += wp[1]*steps

    if h == N:
        wp[1] += steps
    if h == W:
        wp[0] -= steps
    if h == S:
        wp[1] -= steps
    if h == E:
        wp[0] += steps

def solve2():
    global instr, right, up, wp
    for i in instr:
        move2(i[0], i[1])
    print(abs(right)+abs(up))

solve()
# (east, north)
wp, right, up = [10, 1], 0, 0
solve2()
