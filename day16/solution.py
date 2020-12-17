input = 'input'

with open(input) as f:
    parts = f.read().split('\n\n')

rules = [s.split(':')[1].strip() for s in parts[0].split('\n')]

allowed = set()
for rule in rules:
    for ranges in rule.split(' or '):
        lower, upper = ranges.split('-')
        for number in range(int(lower), int(upper) +1 ):
            allowed.add(number)

fields = [int(i) for i in parts[2].strip().split(':\n')[1].replace('\n', ',').split(',')]

not_allowed = []
for f in fields:
    if f not in allowed:
        not_allowed.append(f)

print(sum(not_allowed))