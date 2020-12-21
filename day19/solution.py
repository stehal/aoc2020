import copy
input = 'input'

with open(input) as f:
    rules, messages_received = f.read().split('\n\n')

rulemap = {}
for rule in rules.split("\n"):
    nr, value =rule.split(':')
    rulemap[nr] = value.strip().strip('"')

all = []

def gen(message, messages):
    for i, item in enumerate(message):
        if item not in ['a', 'b']:
            parts = []
            p = rulemap[item]
            if '|' in  p:
                parts=p.split('|')
            else:
                parts.append(p)
        
            for part in parts:
                part.strip()
                mm = copy.copy(message)
                rules = part.split()
                rules.reverse()
                mm.pop(i)
                for rule in rules:
                    mm.insert(i, rule)
                messages.append(mm)
            return

def doit(messages):    
    while len(messages):
        message = messages.pop()
        digits=[s.isdigit() for s in message]  
        if not any(digits):
            all.append(''.join(message))
        else:
            gen(message, messages)

m31 = [['31']]
doit(m31)
a31 = copy.copy(all)
s31 = set(a31)

all = []

m42 = [['42']]
doit(m42)
a42 = copy.copy(all)
s42 = set(a42)

x = 8
count=0
  
for message in messages_received.split('\n'):
    count42 = 0
    count31 = 0
    b=3
    for i in range(b):
        byte = message[i*x:(i+1) * x]
        if byte in s42 and count31 == 0:
            count42+= 1
        elif byte in s31:
            count31 += 1
    if count42 + count31 == b and count42>count31 and count31:
        count+=1
print("part1", count)

count=0

for message in messages_received.split('\n'):
    b = len(message)/x
    count42 = 0
    count31 = 0
    for i in range(b):
        byte = message[i*x:(i+1) * x]
        if byte in s42 and count31 == 0:
            count42+= 1
        elif byte in s31:
            count31 += 1
    if count42 + count31 == b and count42>count31 and count31:
        count+=1
print("part2", count)

      
      

    




