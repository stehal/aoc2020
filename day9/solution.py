infile = "input"
j = 25

n = [int(s) for s in open(infile)]

def sums(p, start):
    ss = n[start:start + p]
    s = set()
    for x in ss:
        for y in ss:
            s.add(x+y)
    return s

for i in range(len(n)):
    s = sums(j,i)
    if n[j] not in s:
        w = n[j]
        break
    j += 1 

print("part 1", w)

for i in range(len(n)):
    j = i
    sum = 0
    while sum < w:
        sum += n[j]
        j += 1
    if sum == w:
        print("part 2", max(n[i:j]) + min(n[i:j]))
        break


     
    
	
	