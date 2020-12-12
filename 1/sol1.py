import re

def solve2():
    with open('input') as f:
        numbers = [int(i) for i in f.readlines()]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)-1):
                for k in range(j+1, len(numbers)-1):
                    if numbers[i] + numbers[j] + numbers[k] == 2020:
                        return numbers[i]*numbers[j]*numbers[k]

def solve1():
    with open('input') as f:
        numbers = [int(i) for i in f.readlines()]
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)-1):
                if numbers[i]+numbers[j] == 2020:
                    return numbers[i]*numbers[j]

print(solve1())
print(solve2())
