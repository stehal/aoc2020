import numpy as np
import copy

with open('input') as f:
    tilestrings = f.read().split('\n\n')
    
alltiles={}

for tilestring in tilestrings:
    tile = []
    for i, s in enumerate(tilestring.split('\n')):
        if i ==0:
            number = int(s.split()[1].strip(':'))
        else:
            tile.append(list(s))
    alltiles[number] = np.array(tile,str)


#find corner tiles
def sides(tilenumber):
    sides = []
    tile=alltiles[tilenumber]
    sides.append(''.join(tile[0]))
    sides.append(''.join(tile[:,-1]))
    sides.append(''.join(tile[-1]))
    sides.append(''.join(tile[:,0]))
    for i in range(4):
        sides.append(''.join(reversed(sides[i])))
    return sides

def matchsides(tilenumber):
    allothersides = set()
    for matchtilenumber, matchtile in alltiles.items():
        if matchtilenumber != tilenumber:
            allothersides.update(sides(matchtilenumber))
    matchingsides=[]
    for side in sides(tilenumber):
        if side in allothersides:
            matchingsides.append(side)
    return matchingsides

def findcorners():
    ctn = []
    for tilenumber, tile in alltiles.items():
        if len(matchsides(tilenumber))==4:
            ctn.append(tilenumber)
    return ctn

r = 1
corners = findcorners()
for c in corners:
    r *= c
print("part 1",r)

#choose a corner (top left) and make jigsaw row by row
cornertilenumber = corners[0]
sidematches = matchsides(cornertilenumber)

nonmatchsideindex = []
for i, side in enumerate(sides(cornertilenumber)):
    if side not in sidematches:
        nonmatchsideindex.append(i)

cornertile = alltiles[cornertilenumber]

for i in range(nonmatchsideindex[1]):
    cornertile = np.rot90(cornertile)

def rhs(arr):
    return ''.join(arr[:,-1])

def lhs(arr):
    return ''.join(arr[:,0])

alltiles.pop(cornertilenumber)

def row(starttile):
    row = starttile
    rh = rhs(row)
    foundtilenumber = 1
    while foundtilenumber:
        if not alltiles.items():
            return row

        for tileno, tile in alltiles.items():
            foundtilenumber = 0
            for i in range(4):
                mirrortile = np.fliplr(tile)
                
                if lhs(tile) == rh:
                    foundtile = tile
                    foundtilenumber = tileno
                    break
                elif lhs(mirrortile) == rh:
                    foundtile = mirrortile
                    foundtilenumber = tileno
                    break
                tile = np.rot90(tile)

                mirrortile = np.rot90(mirrortile)
            if foundtilenumber:
                alltiles.pop(tileno)
                row = np.append(row, foundtile, axis=1)
                rh = rhs(row)
                break
    return row

def bottomrow(tile):
    return ''.join(tile[-1])

def toprow(tile):
    return ''.join(tile[0])

def findnextstart(previousstart):
    bottom = bottomrow(previousstart)
    foundtilenumber= 0
    for tileno, tile in alltiles.items():
        for i in range(4):
            mirrortile = np.fliplr(tile)
            if toprow(tile) == bottom:
                foundtile = tile
                foundtilenumber = tileno
                break
            elif toprow(mirrortile) == bottom:
                foundtile = mirrortile
                foundtilenumber = tileno
                break
            tile = np.rot90(tile)
            mirrortile = np.rot90(mirrortile)
        if foundtilenumber:
            alltiles.pop(tileno)
            return foundtile


starttile = cornertile
arr=row(starttile)
for i in range(1,12):
    starttile= findnextstart(starttile)
    newrow = row(starttile)
    arr = np.append(arr,newrow, axis= 0)

#delete edges
todel = []
for i in range(12):
    todel.append(i *10)
    todel.append(i * 10+9)
todel.reverse()

for i in todel:
    arr = np.delete(arr, obj=i, axis=0)
    arr = np.delete(arr, obj=i, axis=1)

#find monsters
monsterstr='''                  # 
#    ##    ##    ###
 #  #  #  #  #  # '''

monster = []
for i, line in enumerate(monsterstr.split('\n')):
    for j, c in enumerate(line):
        if c == '#':
            monster.append([i,j])


def countmonsters(a):
    count = 0
    for i in range(len(arr) -3):
        for j in range(len(arr)- 20):
            found = []
            for m in monster:
                try:
                    found.append(a[i + m[0],j+m[1]] == '#')
                except:
                    found.append(False)
            if all(found):
                count +=1
    return count


allarr = []
a = copy.copy(arr)
for i in range(4):
    a = np.rot90(a)
    allarr.append(a)

b = np.fliplr(arr)

for i in range(4):
    b = np.rot90(b)
    allarr.append(b)

# count number of monsters found
count = 0
for a in allarr:
    c =countmonsters(a)
    count += c

# count number hashes in jigsaw
totalhash = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i,j] == '#':
            totalhash += 1


print("part 2", totalhash - count * len(monster))






    










       


    

            





