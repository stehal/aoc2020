infile = "in.txt"
n = set()

for s in open(infile):
	n.add(int(s))

for i in n:
    x = 2020 - i
    if x in n :
        print(i*x)
        quit()
	
	
	