infile = "input"

def check(keys):
     return len(keys) == 8 or (len(keys) == 7 and "cid" not in keys)

count = 0
keys = set()

for s in open(infile):
    s = s.strip()
    if s == "":
        count += check(keys)
        keys = set()
    else:
        entries = s.split(" ")
        [keys.add(e.split(":")[0]) for e in entries]
 
count += check(keys)
print(count)




        


 


	
	