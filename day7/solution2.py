from collections import defaultdict
infile = "input"

is_contained_by = defaultdict(set)

def parse(s):
    if "no other" in s:
        return
    a =s.replace(" bags contain ", ",").replace(" bags.", "").replace(" bag.", "").replace(" bags", ",").replace(" bag", ",").replace(".", "").replace(", ", ",").replace(",,", ",").strip().split(",")
    k = a[0]
    for i in range(1,len(a)):
        v = (int(a[i].split()[0]), a[i].split()[1] + " " + a[i].split()[2])
        is_contained_by[k].add(v)

[parse(s) for s in open(infile)]

def walk(g, count, x):
    for c in is_contained_by[g]:
        count.append(x * c[0])
        walk(c[1], count,  x * c[0])
    return count

print(sum(walk("shiny gold", [], 1)))

