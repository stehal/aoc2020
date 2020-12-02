infile = "in.txt"

def check(pos1, pos2, letter, pwd):
    return (pwd[int(pos1) -1] == letter) != (pwd[int(pos2) -1] == letter)
        
def parse(s):
    t = s.replace("-", " ").replace(":", "").split()
    return  check(*t)
 
print(sum([parse(s) for s in open(infile)]))


	
	