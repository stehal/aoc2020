import copy
from collections import deque
from itertools import islice

with open('input') as f:
    playersstr = f.read().split('\n\n')

player1 = deque([int(c) for c in playersstr[0].split('\n')[1:]])
player2 = deque([int(c) for c in playersstr[1].split('\n')[1:]])


def rounds(player1, player2):
    previous = set()
    while True:
        if len(player2) == 0:
            return 1, player1
        if len(player1) == 0:
            return 2, player2
        if (tuple(player1), tuple(player2)) in previous:
            return 1, player1
        previous.add((tuple(player1), tuple(player2)))

        c1 = player1.popleft()
        c2 = player2.popleft()
      
        if len(player1) >=c1 and len(player2) >= c2:
            winner, wincards = rounds(deque(islice(player1,0,c1)).copy(), deque(islice(player2,0,c2)).copy())
            if winner == 1:
                player1.append(c1)
                player1.append(c2)
            else:
                player2.append(c2)
                player2.append(c1)
        else:
            if c1 > c2:
                player1.append(c1)
                player1.append(c2)
            else:
                player2.append(c2)
                player2.append(c1)
       
winner, wincards= rounds(player1.copy(), player2.copy())
result = 0
for i in range(len(wincards)):
    result +=(len(wincards) - i) * wincards[i]

print(result)