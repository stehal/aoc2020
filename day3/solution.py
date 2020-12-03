infile = "in.txt"

m = []     

def parse(s):
    m.append(s.strip() * 120)
    
[parse(s) for s in open(infile)]

h = len(m)

def travers(r, d):
    t, x, y = 0, 0, 0
    while y + d < h:
        if m[y+ d][x + r] == '#':
            t += 1
        x = x + r
        y = y + d
    return t
    
print("sol 1", travers(3,1))    
print("sol 2", travers(1,1) * travers(3,1) * travers(5,1) * travers(7,1) * travers(1,2) )
        


 


	
	