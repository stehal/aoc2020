from collections import Counter
infile = "input"

j = sorted([int(n.strip()) for n in open(infile)])
k = Counter(b-a for a,b in zip(j, j[1:]))
print((k[1] + 1) * (k[3] +1))


     
    
	
	