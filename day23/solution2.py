cupstr='952316487'
upperlimit = 1000000
rounds = 10000000
circlelist = [int(c) for c in cupstr]
for i in range(len(circlelist) + 1,upperlimit + 1):
    circlelist.append(i)
circle = dict(zip(circlelist, circlelist[1:] + circlelist[:1]))

currentcup = circlelist[0]

for move in range(1, rounds +1):
    selected = []
    cup = currentcup
    while len(selected) < 3:
        cup =circle[cup]
        selected.append(cup)
        destination = currentcup -1
    circle[currentcup] = circle[selected[2]]
    while destination in selected:
        destination -= 1
    if destination == 0:
        destination = upperlimit
        while destination in selected:
            destination -= 1
    circle[selected[2]] = circle[destination]
    circle[destination] = selected[0]
    currentcup = circle[currentcup]

x = circle[1]
y = circle[x]
print(x*y)