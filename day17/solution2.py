input ="input"

def to_base3(n): 
    return "0" if not n else to_base3(n//3).lstrip("0") + str(n%3)

b3 = [to_base3(n).zfill(4) for n in range(81)]
b3int = [(int(number[0]) - 1, int(number[1]) -1,int(number[2])-1,int(number[3] )-1) for number in b3]

def surrounding(a):
    return {(a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3]) for b in b3int if b[0] or b[1] or b[2] or b[3] }

matrix_active = set()

x,z,w=0,0,0
for s in open(input):
    y = 0
    for a in s.strip():
        if a=="#":
            matrix_active.add((x,y,z,w))
        y += 1
    x +=1

def doit(times,  matrix_active):
    while times > 0:
        times -= 1
        new_matrix, new_active = set(), set()
        for p in matrix_active:
            for c in surrounding(p).union({p}):
                if c in matrix_active and 2 <= len(matrix_active.intersection(surrounding(c))) <=3:
                    new_active.add(c)
                if c not in matrix_active and len(matrix_active.intersection(surrounding(c))) ==3:
                    new_active.add(c)
        matrix_active = new_active
    return new_active

print("active", len(doit(6, matrix_active)))