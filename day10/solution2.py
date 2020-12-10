from collections import defaultdict
infile = "input"

j = [int(n.strip()) for n in open(infile)]
j.append(0)
j.sort()
j.append(j[-1]+ 3)

paths = []
p = [0]
for i, v in enumerate(j):
    if i + 1 == len(j):
        break
    p.append(j[i+1])
    if j[i+1] - j[i] == 3:
        paths.append(p)
        p=[j[i+1]]

def gr(pp):
    s=defaultdict(list)
    for i, a in enumerate(pp):
        for j in range(1,len(pp)):
            if pp[j]-a <=3 and pp[j] -a > 0:
                s[a].append(pp[j])
    return s

def traverse(g, start, finish, t):
    for n in g[start]:
        traverse(g,n, finish, t)
        if n == finish:
            t.append(1)
    return t

a = 1
for pp in paths:
    s = gr(pp)
    t = traverse(s, min(s.keys()), max(s.keys()) ,[] )
    if t:
        a *= sum(t)

print(a)
    
   




        


     
    
	
	