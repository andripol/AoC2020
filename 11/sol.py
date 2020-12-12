FREE = "L"
FLOOR = "."
OCC = "#"

m = [l.strip('\n') for l in open("input").readlines()]

def adj(i, j):
    global m
    a  = []
    ri = i+2 if i+2<len(m) else len(m)
    rj = j+2 if j+2<len(m[0]) else len(m[0])
    li = i-1 if i-1>0 else 0
    lj = j-1 if j-1>0 else 0
    for k in range(li, ri):
        for l in range(lj, rj):
            a.append(m[k][l])
    return a

def adj2(i, j):
    global m
    a  = []
    f = False
    # right
    rj = j+1
    k = rj
    while k < len(m[0]) and (not f):
        if m[i][k] != FLOOR:
            a.append(m[i][k])
            f = True
        k += 1

    # left
    f = False
    lj = j-1
    k = lj
    while k > -1 and (not f):
        if m[i][k] != FLOOR:
            a.append(m[i][k])
            f = True
        k -= 1

    # up
    f = False
    li = i-1
    k = li
    while k > -1 and (not f):
        if m[k][j] != FLOOR:
            a.append(m[k][j])
            f = True
        k -= 1

    # down
    f = False
    ri = i+1
    k = ri
    while k < len(m) and (not f):
        if m[k][j] != FLOOR:
            a.append(m[k][j])
            f = True
        k += 1

    # ul
    f = False
    k, l = li, lj
    while k > -1 and l > -1 and (not f):
        if m[k][l] != FLOOR:
            a.append(m[k][l])
            f = True
        k -= 1
        l -= 1

    #ur
    f = False
    k, l = li, rj
    while k > -1 and l < len(m[0]) and (not f) :
        if m[k][l] != FLOOR:
            a.append(m[k][l])
            f = True
        k -= 1
        l += 1


    # dl
    f = False
    k, l = ri, lj
    while k < len(m) and l > -1 and (not f) :
        if m[k][l] != FLOOR:
            a.append(m[k][l])
            f = True
        k += 1
        l -= 1

    #dr
    f = False
    k, l = ri, rj
    while k < len(m) and l < len(m[0]) and (not f):
        if m[k][l] != FLOOR:
            a.append(m[k][l])
            f = True
        k += 1
        l += 1

    return a


def solve():
    global m
    while True:
        prev = m[:]
        nxt = m[:]
        for i in m:
            print(i)
        print()
        for i in range(len(m)):
            for j in range(len(m[0])):
                a = adj(i,j)
                if m[i][j] == FREE and a.count(OCC) == 0:
                    temp = list(nxt[i])
                    temp[j] = OCC
                    nxt[i] = "".join(temp)
                elif m[i][j] == OCC:
                    if a.count(OCC) >= 5:
                        temp = list(nxt[i])
                        temp[j] = FREE
                        nxt[i] = "".join(temp)
        if nxt == prev:
            return sum([i.count(OCC) for i in nxt])
        m = nxt[:]

def solve2():
    global m
    while True:
        prev = m[:]
        nxt = m[:]
        for i in range(len(m)):
            for j in range(len(m[0])):
                a = adj2(i,j)
                if m[i][j] == FREE and a.count(OCC) == 0:
                    temp = list(nxt[i])
                    temp[j] = OCC
                    nxt[i] = "".join(temp)
                elif m[i][j] == OCC:
                    if a.count(OCC) >= 5:
                        temp = list(nxt[i])
                        temp[j] = FREE
                        nxt[i] = "".join(temp)
        if nxt == prev:
            return sum([i.count(OCC) for i in nxt])
        m = nxt[:]




#print(solve())
print(solve2())
