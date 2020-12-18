lines = [i.strip() for i in open("input").readlines()]

def operate(n1, n2, op):
    res = n1 + n2 if op == '+' else n1*n2
    return res

def count_line(l):
    i, op, count = 0, '+', 0
    while i < len(l):
        if l[i] == '(':
            j = i + 1
            subexpr = []
            count_par = 1
            while l[j] != ')' or count_par > 1:
                if l[j] == '(':
                    count_par += 1
                if l[j] == ')':
                    count_par -= 1
                subexpr.append(l[j])
                j += 1
            res = count_line("".join(subexpr))
            count = operate(count, res, op)
            i += len(subexpr) + 1
            continue
        elif l[i].isdigit():
            count = operate(count, int(l[i]), op)
        else:
            op = l[i]
        i += 1
    return count

def solve(lines):
    sums = []
    for l in lines:
        sums.append(count_line(l))
    print(sum(sums))

def find_idx_of_plus(l, plus):
    count_plus = 0
    idx = 0
    while count_plus != plus:
        idx += 1
        if l[idx] == '+':
            count_plus += 1
    return idx

def find_prev_chunk(l, plus):
    i = find_idx_of_plus(l, plus) - 1
    if l[i].isdigit():
        return i
    # )
    count_par = 0
    while not (l[i] == '(' and count_par == 1):
        if l[i] == ')':
            count_par += 1
        if l[i] == '(':
            count_par -= 1
        i -= 1
    return i

def find_next_chunk(l, plus):
    i = find_idx_of_plus(l, plus) + 1
    if l[i].isdigit():
        return i
    # (
    count_par = 0
    while not (l[i] == ')' and count_par == 1):
        if l[i] == '(':
            count_par += 1
        if l[i] == ')':
            count_par -= 1
        i += 1
    return i

def solve2():
    edited_input = []
    for l in lines:
        par_l = [i for i in l]
        offset = 0
        count_plus = 0
        for i in range(len(l)):
            if l[i] == '+':
                count_plus += 1
                idx = find_prev_chunk(par_l, count_plus)
                par_l.insert(idx, '(')
                idx = find_next_chunk(par_l, count_plus)
                par_l.insert(idx+1, ')')
        edited_input.append("".join(par_l))
    solve(edited_input)

solve(lines)
solve2()
