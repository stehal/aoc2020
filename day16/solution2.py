from collections import defaultdict
input = 'input'

with open(input) as f:
    parts = f.read().split('\n\n')

all_allowed = set()
allowed = defaultdict(set)
for line in parts[0].split('\n'):
    name, rule = line.strip().split(":")
    for ranges in rule.split(' or '):
        lower, upper = ranges.split('-')
        for number in range(int(lower), int(upper) +1 ):
            allowed[name].add(number)
            all_allowed.add(number)

my_ticket = [int(i) for i in parts[1].strip().split('\n')[1].split(',')]

nearby_tickets = []
for ticket in [t.split(',') for t in parts[2].strip().split(':\n')[1].split('\n')]:
    found = True
    nt =  [int(i) for i in ticket]
    for field in nt:
        if field not in all_allowed:
            found = False
    if found:
        nearby_tickets.append(nt)

allocated = set()
done = {}
while len(allocated) < len(nearby_tickets[0]):
    for position in range(len(nearby_tickets[0])):
        if position not in done.keys():
            ss=[]
            for nt in nearby_tickets:
                possible = set()
                for k,v in allowed.items():
                    if nt[position] in v:
                        possible.add(k)
                ss.append(possible)
         
            inters = set.intersection(*ss)
            inters.difference_update(allocated)
            if len(inters) == 1:
                field = inters.pop()
                allocated.add(field)
                done[position] =  field

chosen = 1
for i ,v in done.items():
    if v[:9] == "departure":
        chosen *= my_ticket[i]
print("answer", chosen)