import copy
import collections

input = "input"
def split(word): 
    return [char for char in word]

seats = [split(s.strip()) for s in open(input)]
#print(seats)
h = len(seats)
w = len(seats[0])

def check(i,j, seats):
    adj = []
    #check north
    ii = i - 1
    jj = j
    while ii >= 0:
        if seats[ii][jj] != '.':
            adj.append(seats[ii][jj])
            break
        ii -= 1
    #check south
    ii = i + 1
    jj = j
    while ii < h:
        if seats[ii][jj] != '.':
            adj.append(seats[ii][jj])
            break
        ii += 1
    
    #check west
    ii = i
    jj = j - 1
    while jj >=0:
        if seats[ii][jj] != '.':
            adj.append(seats[ii][jj])
            break
        jj -=1
    
    #check east
    ii = i
    jj = j + 1
    while jj < w:
        if seats[ii][jj] != '.':
            adj.append(seats[ii][jj])
            break
        jj += 1

    #check ne
    ii = i - 1
    jj = j + 1
    while ii >= 0 and jj < w:
        if seats[ii][jj] != '.':
            adj.append(seats[ii][jj])
            break
        ii -= 1
        jj += 1

    #check se
    ii = i + 1
    jj = j + 1
    while ii < h and jj < w:
        if seats[ii][jj] != '.':
            adj.append(seats[ii][jj])
            break
        ii += 1
        jj += 1

    #check sw
    ii = i + 1
    jj = j - 1
    while ii < h and jj >=0:
        if seats[ii][jj] != '.':
            adj.append(seats[ii][jj])
            break
        ii += 1
        jj -= 1

    #check nw
    ii = i - 1
    jj = j - 1
    while ii >=0 and jj >=0:
        if seats[ii][jj] != '.':
            adj.append(seats[ii][jj])
            break
        ii -= 1
        jj -= 1
                
    return collections.Counter(adj)

def seat(seats):
    newseats = copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            c = check(i,j, seats)
            if seats[i][j] == 'L' and c['#'] == 0:
                newseats[i][j] = "#"
            elif seats[i][j] == '#' and c['#'] >= 5:
                newseats[i][j] = "L"
    return newseats
            
count = 0            


while 1 == 1:
    newseats = seat(seats)
    if newseats == seats:
        c = 0
        for x in newseats:
            for y in x:
                if y == "#":
                    c+=1
        print(c)
        break
    count += 1    
    seats = newseats
