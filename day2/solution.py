infile = "in.txt"
    
def check(min, max, letter, pwd):
    count = pwd.count(letter)
    return (int(min) <= count) and (int(max) >= count)

def parse(s):
    t = s.replace("-", " ").replace(":", "").split()
    return  check(*t)

print(sum([parse(s) for s in open(infile)]))


	
	