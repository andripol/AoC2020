import copy
from collections import defaultdict

deck, deck1, deck2 = [], [], []
for i in open('input').readlines()[1:]:
    if i.find("Player 2:") != -1:
        deck1 = copy.deepcopy(deck)
        deck.clear()
        continue
    if i.strip() == "":
        continue
    deck.append(int(i.strip()))
deck2 = copy.deepcopy(deck)

def get_current_image(l1, l2):
    tmp = copy.deepcopy(l1)
    tmp.append(-1)
    tmp.extend(l2)
    return tmp

PLAYER1 = "Player 1"
PLAYER2 = "Player 2"

def recursive_combat(deck1, deck2):
    hashmap = {}
    c_round = -1
    while True:
        c_round += 1
        if len(deck1) == 0 or len(deck2) == 0:
            res = (PLAYER2, deck2) if len(deck1) == 0 else (PLAYER1, deck1)
            return res
        if get_current_image(deck1, deck2) in hashmap.values():
            # see also what happens with the remaining cards o player2
            return PLAYER1, deck1
        else:
            hashmap[c_round] = get_current_image(deck1, deck2)
        if deck1[0] <= len(deck1[1:]) and deck2[0] <= len(deck2[1:]):
            winner, deck = recursive_combat(deck1[1:1+deck1[0]], deck2[1:1+deck2[0]])
            if winner == PLAYER1:
                winning = deck1.pop(0)
                losing = deck2.pop(0)
                deck1.extend([winning, losing])
            else:
                winning = deck2.pop(0)
                losing = deck1.pop(0)
                deck2.extend([winning, losing])
        elif deck1[0] >= deck2[0]:
            winning = deck1.pop(0)
            losing = deck2.pop(0)
            deck1.extend([winning, losing])
        else:
            winning = deck2.pop(0)
            losing = deck1.pop(0)
            deck2.extend([winning, losing])

def solve2():
    winner, deck = recursive_combat(deck1, deck2)
    print("Winner's points: ", sum([deck[len(deck) - i - 1]*(i+1) for i in range(len(deck))]))

solve2()
