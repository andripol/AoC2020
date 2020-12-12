ads = [int(i) for i in open("input").readlines()]
ads.insert(0, 0)
ads.sort()
ads.append(ads[-1] + 3)

def solve():
    dif = {1: 0, 3: 1}
    ways = 1
    dic = {0: 1}
    for j in range(1, len(ads)):
        if ads[j] - ads[j-1] == 1:
            dif[1] += 1
        elif ads[j] - ads[j-1] == 3:
            dif[3] = dif[3] + 1

        count = dic[j-1]
        for k in range(j-2, -1, -1):
            if ads[j] - ads[k] < 4:
                count += dic[k]
            else:
                break
        dic[j] = count

    print("Sol2: ", dic[len(ads)-1])
    print("Sol1 :", dif[1]*dif[3])

solve()




