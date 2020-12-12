from operator import add

#### binary search ####
def solve():
    bps = [s.strip() for s in open('input').readlines()]
    cols = [s[:7] for s in bps]
    seats = [s[7:] for s in bps]
    col_n, seat_n = [], []
    for c in cols:
        min_c = 0
        max_c = 127
        for i in range(len(c)):
            if (max_c - min_c == 1):
                if c[i] == 'B':
                    col_n.append(max_c)
                else:
                    col_n.append(min_c)
            if c[i] == 'B':
                min_c = int((min_c+max_c)/2) + 1
            else:
                max_c = int((min_c+max_c)/2)

    for s in seats:
        min_s = 0
        max_s = 7
        for i in range(len(s)):
            if (max_s - min_s == 1):
                if s[i] == 'R':
                    seat_n.append(max_s)
                else:
                    seat_n.append(min_s)
            if s[i] == 'R':
                min_s = int((min_s+max_s)/2) + 1
            else:
                max_s = int((min_s+max_s)/2)

    l = [i*8 for i in col_n]
    l = list( map(add, seat_n, l) )
    l.sort()

    for i in range(1, len(l)):
        if abs(l[i] - l[i-1]) > 1:
            print(l[i] - 1)
            break

    print(max(l))

### oooorr... ###
def convert(s):
    s = s.replace('B','1')
    s = s.replace('R','1')
    s = s.replace('F','0')
    s = s.replace('L','0')
    return s

def solve2():
    bps = [s.strip() for s in open('input').readlines()]
    cols = [int(convert(s[:7]), 2) for s in bps]
    seats = [int(convert(s[7:]), 2) for s in bps]

    l = list( map(add, seats, [i*8 for i in cols]) )
    print(max(l))

    l.sort()
    for i in range(1, len(l)):
        if abs(l[i] - l[i-1]) > 1:
            print(l[i] - 1)
            break

solve()
solve2()
