input = 'input'

with open (input) as f:
    data=f.read().split()

busses = [int(b) for b in data[1].replace("x,",'').split(',')]

mins = []
for i,b in enumerate(data[1].split(',')):
    if b != 'x':
        mins.append(i)

def round(a,b,bm, g):
    count = 0
    while ((a + (g * count)) % b) != (b - bm)%b:
        count +=1
    return a + g*count

g = 1
a=busses[0]
for z in zip(busses, mins):
    a = round(a, z[0], z[1], g)
    g = g*z[0]

print("Solution", a)   