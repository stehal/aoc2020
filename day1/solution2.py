infile = "in.txt"
set_n = set()

for s in open(infile):
	set_n.add(int(s))

for i in set_n:
    for j in set_n.difference({i}):
        x = 2020 - i - j
        if x in set_n.difference({i, j}) :
            print(i*j*x)
            quit()
	
	
	