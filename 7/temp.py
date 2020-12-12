def solve():
    rules = [s.strip('\n | .').split(' bags contain ') for s in open('sample').readlines()]
    temp = []
    for r in rules:
        temp.append([r[0], [i.strip('bags | bag') for i in r[1].split(', ')]])
    rules = temp

    rules_d = {}
    for r in rules:
        temp = []
        for i in r[1]:
            i2 = i
            h = i2.strip('0|1|2|3|4|5|6|7|8|9| ')
            if i[:-len(h)].strip() == "":
                t = 0
            else:
                t = int(i[:-len(h)].strip())
            temp.append((h,t))
        rules_d[r[0]] = temp
