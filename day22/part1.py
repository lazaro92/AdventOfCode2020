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

def play(data):
    player1, player2 = data

    rounds = 0
    while(len(player1) > 0 and len(player2) > 0):
        rounds += 1
        c1 = player1.pop()
        c2 = player2.pop()
        if c1 > c2:
            player1.appendleft(c1)
            player1.appendleft(c2)
        else:
            player2.appendleft(c2)
            player2.appendleft(c1)

    if len(player1) > 0:
        return player1
    else:
        return player2

def calc_result(deck):
    x = 1
    acc = 0
    for card in deck:
        acc += x * card
        x += 1
    return acc

data = read_input()
deck = play(data)
print(calc_result(deck))
