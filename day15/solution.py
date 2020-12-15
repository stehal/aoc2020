from collections import defaultdict
#part 1 length=2020
#part 2
length = 30000000
numbers=[6,19,0,5,7,13,1]

pos = defaultdict(list)

for i, n in enumerate(numbers):
    pos[n].append(i + 1)

while True:
    lastnumber = numbers[-1]
    if len(pos[lastnumber]) > 1:
        new_num = len(numbers) - pos[lastnumber][-2]
    else:
        new_num = 0
    
    numbers.append(new_num)
    pos[new_num].append(len(numbers))
    if len(numbers) == length:
        print(numbers[- 1])
        break

    

