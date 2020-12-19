[rules, words] = [i for i in open('input2').read().split('\n\n')]

rules_d = {}
for i in rules.split('\n'):
    key, value = i.split(':')
    key, value = int(key.strip()), [j.strip(' ') for j in value.strip().split('|')]
    value = [j if j.isalpha() else list(map(int, j.split(' '))) for j in value]
    rules_d[key] = value
rules = rules_d

def obey_rules_rec(word, rule):
    if len(rule) == 1:
        if len(word) == 0:
            return "False"
        if type(rule[0]) == str:
            if word[0] == rule[0]:
                if len(word) > 1 and len(rule[0]) > 1:
                    return obey_rules_rec(word[1:], [rule[1:]])
                elif len(word) > 1:
                    return word[1:]
                else:
                    return ""
            else:
                return "False"
        else:
            new_word = word
            for r in rule[0]:
                word = new_word
                new_word = obey_rules_rec(word, rules[r])
                if new_word == "False":
                    return "False"
            return new_word
    else:
        word1 = obey_rules_rec(word, [rule[0]])
        if word1 == "False":
            word2 = obey_rules_rec(word, [rule[1]])
            if word2 == "False":
                return "False"
            elif len(word2) > 0:
                return word2
        elif len(word1) > 0:
            return word1
        return ""

def obey_rules(word, rule):
    if obey_rules_rec(word, rule) == "":
        return True
    return False

word_d = {}
for w in words.strip().split('\n'):
    word_d[w] = 1

def solve(rule):
    global word_d
    count = 0
    to_be_deleted = []
    for w in word_d:
        if obey_rules(w, rule):
            count += 1
            to_be_deleted.append(w)

    for w in to_be_deleted:
        del word_d[w]

    return count

print('Sol1: ', solve(rules[0]))

word_d = {}
for w in words.strip().split('\n'):
    word_d[w] = 1

def solve2():
    rule = [42, 42, 31]
    count = solve([rule])
    for eight in range(7):
        rule = [42, 42, 31]
        for i in range(eight):
            rule = [42] + rule
        count += solve([rule])
        for eleven in range(7):
            for j in range(eleven):
                rule = [42] + rule
                rule.append(31)
                count += solve([rule])
    return count

print('Sol 2: ', solve2())
