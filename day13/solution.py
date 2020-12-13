input = 'input'
with open (input) as f:
    data=f.read().split()

arrival = int(data[0])
bus = [int(b) for b in data[1].replace("x,",'').split(',')]

delays = [d - (arrival%d) for d in bus]
min_delay = min(delays)
b = bus[delays.index(min_delay)]

print("Solution", b*min_delay)
