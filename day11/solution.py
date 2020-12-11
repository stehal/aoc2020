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
    for r in range(max(0, i - 1), min(h, i +2 ) ):
        for s in range(max(0, j - 1), min(w, j +2 ) ):
            if r != i or s != j:
                adj.append(seats[r][s])
    return collections.Counter(adj)

def seat(seats):
    newseats = copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            c = check(i,j, seats)
            if seats[i][j] == 'L' and c['#'] == 0:
                newseats[i][j] = "#"
            elif seats[i][j] == '#' and c['#'] >= 4:
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

