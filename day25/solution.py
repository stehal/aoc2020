pk1=11562782
pk2=18108497

def loop(value, pk):
    loopno = 0
    while value != pk:
        loopno += 1
        value = (value * 7) % 20201227
    return loopno

def looptimes(value, subjectnumber, loopno):
    for i in range(loopno):
        value = (value * subjectnumber) % 20201227
    return value
    
value = 1
print(looptimes(value, pk1, loop(value, pk2)))
