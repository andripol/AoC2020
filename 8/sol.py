ACC = 0

ADD = 'acc'
NOP = 'nop'
JMP = 'jmp'

cmds = [[l.strip('\n').split(' ')[0],int(l.strip('\n').split(' ')[1])] for l in open('input').readlines()]

def solve(cmds):
    global ACC, ADD, NOP, JMP
    hist = {}
    ip = 0
    while True:
        if ip in hist.keys():
            return False
        if ip > len(cmds)-1:
            return True
        hist[ip] = 0
        if cmds[ip][0] == ADD:
            ACC += cmds[ip][1]
            ip += 1
            continue
        if cmds[ip][0] == NOP:
            ip += 1
            continue
        if cmds[ip][0] == JMP:
            ip += cmds[ip][1]
            continue

def solve2():
    global ACC, ADD, NOP, JMP, cmds
    for i in cmds:
        ACC = 0
        if i[0] == JMP:
            i[0] = NOP
            if solve(cmds):
                return
            else:
                i[0] = JMP
        if i[0] == NOP:
            i[0] = JMP
            if solve(cmds):
                return
            else:
                i[0] = NOP


solve(cmds)
print(ACC)

solve2()
print(ACC)
