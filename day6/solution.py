infile = "input"

count = 0
y = set()

for s in open(infile):
    s = s.strip()
    if s == "":
        count += len(y)
        y = set()
    else:
        [y.add(a) for a in s]
 
count += len(y)
print(count)




        


 


	
	