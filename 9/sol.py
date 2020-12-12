lines = [int(i) for i in open('input').readlines()]

def check(num, pre):
    for i in range(len(pre)):
        for j in range(i+1, len(pre)):
            if pre[i]+pre[j] == num:
                return True
    return False

def check2(num, pre):
    for i in range(len(pre)):
        count = [pre[i]]
        for j in range(i+1, len(pre)):
            if sum(count)+pre[j] == num:
                return max(count)+min(count)
            count.append(pre[j])
    return 0

def solve(PREAMBLE):
    pre, nums = lines[:PREAMBLE], lines[PREAMBLE:]

    for i in nums:
        if not check(i, pre):
            print(i)
            print(check2(i,lines))
            return
        pre.pop(0)
        pre.append(i)

solve(25)
