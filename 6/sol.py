def solve():
    answers = [''.join(a.split('\n')) for a in open('input').read().split('\n\n')]
    answers = [set(a) for a in answers]
    print(sum(len(a) for a in answers))

def solve2():
    answers = [a.split('\n') for a in open('input').read().split('\n\n')]
    print(answers)
    answers2 = []
    for a in answers:
        answer = set(a[0])
        for b in a[1:]:
            if b == "":
                continue
            answer = answer.intersection(set(b))
        answers2.append(answer)
    print(sum(len(a) for a in answers2))

solve()
solve2()
