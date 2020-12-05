infile = "input"
 
print(max([ int(s.replace("B", "1").replace("R", "1").replace("F", "0").replace("L", "0"),2) for s in open(infile)]))