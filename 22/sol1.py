import copy

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

while True:
    if deck1[0] >= deck2[0]:
        winning = deck1.pop(0)
        losing = deck2.pop(0)
        deck1.extend([winning, losing])
    else:
        winning = deck2.pop(0)
        losing = deck1.pop(0)
        deck2.extend([winning, losing])
    if len(deck1) == 0 or len(deck2) == 0:
        break

deck = deck1 if len(deck2) == 0 else deck2
print("Winner's points: ", sum([deck[len(deck) - i - 1]*(i+1) for i in range(len(deck))]))
