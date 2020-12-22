import collections

def read_input():
    data = []
    with open('input.txt','r') as r:
        player = collections.deque()
        for line in r.read().split('\n'):
            if line.isdigit():
                player.appendleft(int(line))
            elif line == '':
                data.append(player)
                player = collections.deque()
    return data

def play(player1, player2):
    decks1 = []
    decks2 = []
    while(len(player1) > 0 and len(player2) > 0):
        #finish rule
        if player1 in decks1 or player2 in decks2:
            return 1, player1

        decks1.append(player1.copy())
        decks2.append(player2.copy())

        c1 = player1.pop()
        c2 = player2.pop()

        if c1 <= len(player1) and c2 <= len(player2):
            cp1 = player1.copy()
            while c1 != len(cp1):
                cp1.popleft()
            cp2 = player2.copy()
            while c2 != len(cp2):
                cp2.popleft()

            winner,_ = play(cp1, cp2)

            if winner == 1:
                player1.appendleft(c1)
                player1.appendleft(c2)
            elif winner == 2:
                player2.appendleft(c2)
                player2.appendleft(c1)
            continue

        # normal game
        if c1 > c2:
            player1.appendleft(c1)
            player1.appendleft(c2)
        else:
            player2.appendleft(c2)
            player2.appendleft(c1)

    if len(player1) > 0:
        return 1, player1
    else:
        return 2, player2

def calc_result(deck):
    x = 1
    acc = 0
    for card in deck:
        acc += x * card
        x += 1
    return acc

data = read_input()
w, deck = play(data[0], data[1])
print(calc_result(deck))
