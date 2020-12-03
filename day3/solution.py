infile = "in.txt"

m = []     

def parse(s):
    m.append(s.strip() * 120)
    
[parse(s) for s in open(infile)]

h = len(m)
w = len(m[0])

def travers(r, d):
    t = 0
    for x, y in zip(range(r, w, r), range(d, h, d)):
        t +=  (m[y][x] == '#')
    return t
    
print("sol 1", travers(3,1))    
print("sol 2", travers(1,1) * travers(3,1) * travers(5,1) * travers(7,1) * travers(1,2) )
        


 


	
	