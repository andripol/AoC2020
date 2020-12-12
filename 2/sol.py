import re

def solve1():
    valids = 0
    for s in open('input').readlines():
        min, max = (int(i) for i in re.findall(r'\d+', s))
        letter, psw = (i for i in re.findall(r'[A-Za-z]+', s))
        count = sum(c == letter for c in psw)
        valids += count >= min and count <= max
    return valids

def solve2():
    valids = 0
    for s in open('input').readlines():
        ind1, ind2 = (int(i)-1 for i in re.findall(r'\d+', s))
        letter, psw = (i for i in re.findall(r'[A-Za-z]+', s))
        valids += (psw[ind1] == letter) ^ (psw[ind2] == letter)
    return valids

print(solve1())
print(solve2())
