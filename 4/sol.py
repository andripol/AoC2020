import re
import string

def check(fields):
    for f in fields:
        k, v = f.split(':')
        if (k == 'byr') and (int(v) < 1920 or int(v) > 2002 or len(v)!=4 or (not v.isnumeric())):
            return False
        if (k == 'iyr') and (int(v) < 2010 or int(v) > 2020 or len(v)!=4 or (not v.isnumeric())):
            return False
        if (k == 'eyr') and (int(v) < 2020 or int(v) > 2030 or len(v)!=4 or (not v.isnumeric())):
            return False
        if (k == 'hgt'):
            if v[-2:] == 'cm':
                if int(v[:-2]) < 150 or int(v[:-2]) > 193 or (not v[:-2].isnumeric()):
                    return False
            elif v[-2:] == 'in':
                if int(v[:-2]) < 59 or int(v[:-2]) > 76 or (not v[:-2].isnumeric()):
                    return False
            else:
                return False
        if k == 'hcl':
            if v[0] != '#' or len(v) != 7 or (not all(c in string.hexdigits for c in v[1:])):
                return False
        if (k == 'ecl'):
            if v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False
        if (k == 'pid'):
            if (not v.isnumeric()) or len(v) != 9:
                return False
    return True

def solve2():
    s = open('input').read()
    passports = [p for p in s.split('\n\n')]
    count = 0
    for p in passports:
        fields = [f for f in re.split(' |\n', p)]
        if len(fields) >= 8 and check(fields):
            count += 1
        elif len(fields) == 7 and check(fields):
            keys=[]
            for f in fields:
                keys.append(f.split(':')[0])
            if 'cid' not in keys:
                count += 1
    return count

def solve():
    s = open('input').read()
    passports = [p for p in s.split('\n\n')]
    count = 0
    for p in passports:
        fields = [f for f in re.split(' |\n', p)]
        if len(fields) >= 8:
            count += 1
        elif len(fields) == 7:
            keys=[]
            for f in fields:
                keys.append(f.split(':')[0])
            print(keys)
            if 'cid' not in keys:
                count += 1
    return count



print(solve())
print(solve2())
