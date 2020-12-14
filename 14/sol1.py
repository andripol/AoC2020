inp = [[i.split(" = ")[0].strip('memask[] '), i.split(" = ")[1].strip()] for i in open("input").readlines()]

def solve():
    l = []
    for i in inp:
        if i[0] != "":
            l.append([int(i[0]), format(int(i[1]), "b").zfill(36)])
        else:
            l.append([-1, i[1]])

    addresses = {}
    for i in l:
        if i[0] == -1:
            mask = i[1]
        else:
            res = []
            for v in range(len(i[1])):
                if mask[v] == 'X':
                    res.append(i[1][v])
                else:
                    res.append(mask[v])
            addresses[i[0]] = int("".join(res), 2)
    return sum(addresses.values())

print(solve())
