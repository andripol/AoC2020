inp = [[i.split(" = ")[0].strip('memask[] '), i.split(" = ")[1].strip()] for i in open("input").readlines()]

l = []
for i in inp:
    if i[0] != "":
        l.append([int(i[0]), int(i[1])])
    else:
        l.append([-1, i[1]])

def add_addresses_rec(bs, start):
    LENGTH = 35
    addr = 0
    addresses = []
    for i in range(len(bs)):
        if bs[i] != 'X':
            addr += int(bs[i])*(2**(LENGTH - i - start))
        else:
            if (i+1) < len(bs):
                subl = add_addresses_rec(bs[i+1:], start + i + 1)
                for j in subl:
                    addresses.append(addr + 2**(LENGTH - i - start) + j)
                    addresses.append(addr + j)
            else:
                addresses.append(addr + 2**(LENGTH - i - start))
                addresses.append(addr)
            return addresses
    addresses.append(addr)
    return addresses

def solve2():
    addresses = {}
    for i in l:
        if i[0] == -1:
            mask = i[1]
        else:
            value = i[1]
            base_addr = format(i[0], "b").zfill(36)
            res = []
            for v in range(len(base_addr)):
                if mask[v] == 'X' or mask[v] == '1':
                    res.append(mask[v])
                else:
                    res.append(base_addr[v])
            addresses_list = add_addresses_rec(res, 0)
            for j in addresses_list:
                addresses[j] = value

    return sum(addresses.values())

print(solve2())
