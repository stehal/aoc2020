import re

pattern='\d+ \+ \d+'
pattern2='\((\d+)\)'
pattern3='\(\d+( \* \d+){1,}\)'

def evalstr(matchobj):
    return str(eval(matchobj.group(0)))

def strrepl(matchobj):
    return matchobj.group(1)

def evalexp(exp):
    exp1 = exp
    mm = re.search(pattern3, exp)
    while mm:
        exp = re.sub(pattern3, evalstr, exp, 1)
        mm = re.search(pattern3, exp)

    m = re.search(pattern, exp)
    while m:
        exp = re.sub(pattern, evalstr, exp, 1)
        exp = re.sub(pattern2, strrepl, exp )
        mm = re.search(pattern3, exp)
        while mm:
            exp = re.sub(pattern3, evalstr, exp, 1)
            mm = re.search(pattern3, exp)
        m = re.search(pattern, exp)
    return(eval(exp))

sum = 0
for s in open("input"):
    sum += evalexp(s.strip())

print(sum)