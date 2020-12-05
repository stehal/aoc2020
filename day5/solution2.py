infile = "input"
 
all = sorted([ int(s.replace("B", "1").replace("R", "1").replace("F", "0").replace("L", "0"),2) for s in open(infile)])
print([p[0] + 1 for p in zip(all,all[1:]) if p[0] +1 != p[1]])