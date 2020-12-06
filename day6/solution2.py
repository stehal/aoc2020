from collections import defaultdict
infile = "input"

y = defaultdict(int)

def inc(a):
    y[a] += 1

def count(y, n):
    i = 0
    for k,v in y.items():
        if v == n:
            i += 1
    return i

c, n = 0, 0
for s in open(infile):
    s = s.strip()
    if s == "":
        c += count(y, n)
        n = 0
        y = defaultdict(int)
    else:
        [inc(a) for a in s]
        n += 1
 
c += count(y, n)
print(c)




        


 


	
	