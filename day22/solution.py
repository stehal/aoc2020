with open('input') as f:
    playersstr = f.read().split('\n\n')

player1 = [int(c) for c in playersstr[0].split('\n')[1:]]
player2 = [int(c) for c in playersstr[1].split('\n')[1:]]
#playgame
while True:
    c1 = player1.pop(0)
    c2 = player2.pop(0)
    if c1 > c2:
        player1.append(c1)
        player1.append(c2)
    else:
        player2.append(c2)
        player2.append(c1)
    
    if  len(player1) == 0:
        p = player2
        break
    if  len(player2) == 0:
        p = player1
        break

result = 0
for i in range(len(p)):
    result +=(len(p) - i) * p[i]

print(result)