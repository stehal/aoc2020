from collections import defaultdict

s=defaultdict(list)

m =  [4,5,6,7]

for a in m:
    if a  +1 in m:
        s[a].append(a + 1)
    if a  +2 in m:
        s[a].append(a + 2)
    if a  +3 in m:
        s[a].append(a + 3)
   
print(s)

t = []
def traverse(g, start):
    for n in g[start]:
        print("n", n)
        traverse(g,n)
        if n == m[-1]:
            print("add")
            t.append(1)
    return

    

traverse(s, 4)
print(sum(t))




