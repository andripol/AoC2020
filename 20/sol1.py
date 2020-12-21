tiles = [i.strip() for i in open('input').read().split('\n\n')]
ids = [i.split('\n')[0].split(' ')[1].strip(' :') for i in tiles]
ups = [i.split('\n')[1].strip() for i in tiles]
downs = [i.split('\n')[-1].strip() for i in tiles]
lefts = ["".join([j[0] for j in i.split('\n')[1:]]) for i in tiles]
rights = ["".join([j[-1] for j in i.split('\n')[1:]]) for i in tiles]

def solve():
    adj_edges = {}
    for tile in range(len(ids)):
        adj_edges[ids[tile]] = 0
        for idx in range(len(ids)):
            if idx == tile:
                continue
            if ups[tile] == ups[idx] or ups[tile] == downs[idx] or ups[tile][::-1] == ups[idx] or ups[tile][::-1] == downs[idx] or ups[tile] == lefts[idx] or ups[tile] == rights[idx] or ups[tile][::-1] == lefts[idx] or ups[tile][::-1] == rights[idx] or downs[tile] == ups[idx] or downs[tile] == downs[idx] or downs[tile][::-1] == ups[idx] or downs[tile][::-1] == downs[idx] or downs[tile] == lefts[idx] or downs[tile] == rights[idx] or downs[tile][::-1] == lefts[idx] or downs[tile][::-1] == rights[idx]  or lefts[tile] == lefts[idx] or lefts[tile] == rights[idx] or lefts[tile][::-1] == lefts[idx] or lefts[tile][::-1] == rights[idx] or lefts[tile] == ups[idx] or lefts[tile] == downs[idx] or lefts[tile][::-1] == ups[idx] or lefts[tile][::-1] == downs[idx] or rights[tile] == lefts[idx] or rights[tile] == rights[idx] or rights[tile][::-1] == lefts[idx] or rights[tile][::-1] == rights[idx] or rights[tile] == ups[idx] or rights[tile] == downs[idx] or rights[tile][::-1] == ups[idx] or rights[tile][::-1] == downs[idx]:
                adj_edges[ids[tile]] += 1
                #print(ids[tile], ids[idx])

    return(adj_edges)

adj_edges = solve()

count = 1
for key in adj_edges.keys():
    if adj_edges[key] == 2:
        count *= int(key)
print(count)

