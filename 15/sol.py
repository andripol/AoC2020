inp = [int(i) for i in open("input").readline().split(",")]
last_turn = {}
for i in range(len(inp)):
    last_turn[inp[i]] = i+1

def solve():
    current = 0
    current_turn = len(inp)+1
    while True:
        if current_turn == 30000000:
            print(current)
            return
        if current not in last_turn.keys():
            last_turn[current] = current_turn
            current = 0
        else:
            prev = current
            current = current_turn - last_turn[current]
            last_turn[prev] = current_turn
        current_turn += 1

solve(2020)
solve(30000000)
