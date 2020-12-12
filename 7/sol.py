GOLD = 'shinygold'
NO_BAGS = 'noother'

lines = [s.strip('\n .').split(' bags contain ') for s in open('input').readlines()]
rules = []
for r in lines:
    rules.append(["".join(r[0].split()), ["".join(i.strip('.').split()[:-1]) for i in r[1].split(', ')]])

rules_d = {}
for r in rules:
    temp = []
    for i in r[1]:
        h = i.strip('0123456789')
        t = 0 if i[:-len(h)].strip() == "" else int(i[:-len(h)].strip())
        temp.append((h,t))
    rules_d[r[0]] = temp

def contains_gold_r(bag):
    if bag == NO_BAGS:
        return False
    return contains_gold(rules_d[bag])

def contains_gold(bag):
    for i in bag:
        if i[0] == GOLD:
            return True
    for i in bag:
        if contains_gold_r(i[0]):
                return True
    return False

def count_bags_r(bag):
    return count_bags(rules_d[bag])

def count_bags(bag):
    count = 1
    for i in bag:
        if i[0] == NO_BAGS:
            return count
        count += i[1]*count_bags_r(i[0])
    return count

def solve():
    count = 0
    for i in rules_d.keys():
        count += contains_gold(rules_d[i])
    return count

def solve2():
    count = 1
    for i in rules_d[GOLD]:
        count += i[1]*count_bags(rules_d[i[0]])
    return count - 1

print(solve())
print(solve2())
