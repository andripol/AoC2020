[rules, my_ticket, other_tickets] = [i.split('\n') for i in open('input').read().split('\n\n')]

classes = [i.split(':')[0] for i in rules]
rules = [i.split(':')[1].strip().split(' or ') for i in rules]
rules = [[i[0].split('-'), i[1].split('-')] for i in rules]
for i in range(len(rules)):
    for j in range(len(rules[i])):
        for k in range(len(rules[j])):
            rules[i][j][k] = int(rules[i][j][k])

my_ticket = [int(i)  for i in my_ticket[0].split(',')]

other_tickets = other_tickets[:-1]
other_tickets = [[int(j) for j in i.split(',')] for i in other_tickets]

def check(v):
    for i in rules:
        if i[0][0] <= v <= i[0][1] or i[1][0] <= v <= i[1][1]:
            return True
    return False

count = 0
tickets = [my_ticket]
for i in other_tickets:
    flag = True
    for v in i:
        if not check(v):
            count += v
            flag = False
            break
    if flag:
        tickets.append(i)
print(count)

def check_rule(v, ranges):
    if ranges[0][0] <= v <= ranges[0][1] or ranges[1][0] <= v <= ranges[1][1]:
        return True
    return False


dic = {}
for i in range(len(rules)):
    dic[classes[i]] = i

sol = []
for idx in range(len(tickets[0])):
    tmp_dic = dic.copy()
    for t in tickets:
        to_be_removed = {}
        for r in tmp_dic:
            if not check_rule(t[idx], rules[tmp_dic[r]]):
                to_be_removed[r] = 0
        for tbr in to_be_removed:
            tmp_dic.pop(tbr)
    keys = list(tmp_dic.keys())
    if len(keys) == 1:
        k = keys[0]
        dic.pop(k)
        to_be_removed = []
        for s in range(len(sol)):
            sol_dic = sol[s][1]
            if k in sol_dic:
                to_be_removed.append(s)
        for tbr in to_be_removed:
            sol[tbr][1].remove(k)
    sol.append([idx, keys])

def find_final_sol(sol):
    for i in sol:
        keys = i[1]
        if len(keys) == 1:
            k = keys[0]
            to_be_removed = []
            for s in range(len(sol)):
                sol_dic = sol[s][1]
                if k in sol_dic and len(sol_dic) > 1:
                    to_be_removed.append(s)
            for tbr in to_be_removed:
                sol[tbr][1].remove(k)
    return sol

def solve2():
    global sol
    flag = True
    while flag:
        flag = False
        sol = find_final_sol(sol)
        for i in sol:
            keys = i[1]
            if len(keys) > 1:
                flag = True
                break
    deps = [i[0] if i[1][0].find('departure') else -1 for i in sol]
    count = 1
    for i in range(len(deps)):
        if deps[i] == -1:
            count *= my_ticket[i]

    return count

print(solve2())
