def solve(right, down):
    with open('input') as f:
        count = 0
        idx = right
        step = 1
        for s in f.readlines():
            if (step < down):
                step+=1
                continue
            else:
                step = 1
            s = s.strip()
            if (s[idx] == '#'):
                count+=1
            for i in range (right):
                if (len(s)-1 > idx):
                    idx+=1
                else:
                    idx = 0
        return count

def solve2():
    return solve(1,1) * solve(3,1) * solve(5,1) * solve(7,1) * solve(1,2)

print(solve(3,1))
print(solve2())

