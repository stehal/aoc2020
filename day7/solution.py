from collections import defaultdict
infile = "input"

contains = defaultdict(set)
is_contained_by = defaultdict(set)


def parse(s):
    if "no other" in s:
        return
    a =s.replace(" bags contain ", ",").replace(" bags.", "").replace(" bag.", "").replace(" bags", ",").replace(" bag", ",").replace(".", "").replace(", ", ",").replace(",,", ",").strip().split(",")
    k = a[0]
    for i in range(1,len(a)):
        v = a[i].split()[1] + " " + a[i].split()[2]
        is_contained_by[k].add(v)
        contains[v].add(k)


[parse(s) for s in open(infile)]

r = set()

def walk(g):
    for c in contains[g]:
        r.add(c)
        walk(c)
    return


g = "shiny gold"
walk(g)

print(len(r))
