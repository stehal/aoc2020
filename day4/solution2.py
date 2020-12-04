infile = "input"

def checkall(keys):
     return len(keys) == 8 or (len(keys) == 7 and "cid" not in keys)

def checkheight(value):
    try:
        h = int(value[:-2])
    except:
        return False
    m = value[-2:]
    if m == "in" and h >= 59 and h <= 76:
        return True
    if m == "cm" and h >= 150 and h <= 193:
        return True
    return False

def checkhair(value):
    if value[0] != '#':
        return False
    c = value[1:]
    if len(c) != 6:
        return False
    try: 
        int(c, 16)
    except:
        return False
    return True

def checkint(value, l, u):
    try:
        y = int(value)
    except:
        return False
    return y >= l and y <=u

def check(key, value):
    if key == "cid":
        return True
    if key == 'byr' and checkint(value,1920,2002):
        return True
    if key == 'iyr' and checkint(value,2010,2020):
        return True
    if key == 'eyr' and checkint(value,2020,2030):
        return True
    if key == 'hgt':
        if checkheight(value):
            return True
    if key == 'hcl':
        if checkhair(value):
            return True
    if key == 'ecl' and value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return True
    if key == 'pid' and len(value) == 9 and checkint(value,0,999999999):
        return True
    return False

count = 0
keys = set()

for s in open(infile):
    s = s.strip()
    if s == "":
        count += checkall(keys)
        keys = set()
    else:
        entries = s.split(" ")
        for e in entries:
            key, value = e.split(":")
            if check(key, value):
                keys.add(key)

count += checkall(keys)
print(count)




        


 


	
	