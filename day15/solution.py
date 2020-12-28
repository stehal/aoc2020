from collections import defaultdict
def rounds(length, numbers):
    pos = {n:p for p, n in enumerate(numbers[:-1])}
    lastnumberspoken = numbers[-1]
    lastnumberspokenpos = len(numbers) - 1
    for i in range(len(numbers) + 1, length+1):
        if lastnumberspoken in pos:
            new_num = lastnumberspokenpos - pos[lastnumberspoken]
        else:
            new_num = 0
        pos[lastnumberspoken] = lastnumberspokenpos
        lastnumberspoken = new_num
        lastnumberspokenpos +=1
    return new_num
numbers=[6,19,0,5,7,13,1]
print("part 1", rounds( 2020, numbers))
print("part 2", rounds( 30000000, numbers))

    

