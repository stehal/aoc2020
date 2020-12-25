from collections import deque
cupstr='952316487'

circle = [int(c) for c in cupstr]

currentcuplabel = circle[0]
currentcuppos = circle.index(currentcuplabel)

size =len(circle)

def rotate(l, n):
    return l[n:] + l[:n]

def adj(limit):
    if limit >= size:
        limit = limit - size
    return limit

for move in range(1,101):
    selected = []
    for i in range(3):
        popos = currentcuppos + 1
        if popos >= len(circle):
            popos=0
        selected.append(circle.pop(popos))
    destinationcuplabel = currentcuplabel  -1
    while destinationcuplabel in selected:
        destinationcuplabel -= 1
       
    if destinationcuplabel < min(circle):
        destinationcuplabel = max(circle)
    distinationcuppos = circle.index(destinationcuplabel)
    for i, cup in enumerate(selected):
        circle.insert(circle.index(destinationcuplabel)+i +1, cup)
    while currentcuplabel != circle[currentcuppos]:
        circle = rotate(circle,1)
    currentcuppos = (currentcuppos + 1) % len(circle)
    currentcuplabel =circle[currentcuppos]

index = circle.index(1) + 1
print(''.join([str(j) for j in    [circle[(index + i) % len(circle)] for i in range(len(circle) -1)]]))