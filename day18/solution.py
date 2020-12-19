import re

pattern='\d+ (\+|\*) \d+'
pattern2='\((\d+)\)'

def evalstr(matchobj):
    return str(eval(matchobj.group(0)))

def strrepl(matchobj):
    return matchobj.group(1)

def evalexp(exp):
    m = re.search(pattern, exp)
    while m:
        exp = re.sub(pattern, evalstr, exp, 1)
        exp = re.sub(pattern2, strrepl, exp )
        m = re.search(pattern, exp)
    return(eval(exp))

sum = 0
for s in open("input"):
    sum += evalexp( s)

print(sum)