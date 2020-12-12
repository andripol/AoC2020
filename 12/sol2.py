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

def move2(h, steps):
    global instr, right, up, wp
    if (h == L or h == R) and steps == 180:
        wp = [-wp[0], -wp[1]]
    if h == L and steps == 270:
        h, steps = R, 90
    if h == R and steps == 270:
        h, steps  = L, 90
    if h == L and steps == 90:
        wp = [-wp[1], wp[0]]
    if h == R and steps == 90:
        wp = [wp[1], -wp[0]]

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

# wp =  [east, north]
wp, right, up = [10, 1], 0, 0
solve2()
