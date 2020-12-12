input = "input"
pos = [0,0]
dir = 1 #e
compass =  ['N', 'E', 'S', 'W']
dirs = [(1,0), (0,1), (-1,0), (0, -1)] #n,e,s,w

def changedir(dir, inst):
    turns = int(inst[1:]) / 90
    if inst[0] == 'L':
        dir = (dir-turns) % 4
    if inst[0] == 'R':
        dir = (dir+turns) % 4 
    return dir

def move(dir, inst, pos):
    if inst[0] == 'F':
        move_dir = dirs[dir]
    else:
        move_dir = dirs[compass.index(inst[0])]
    pos[0]+=move_dir[0]*int(inst[1:])
    pos[1]+=move_dir[1]*int(inst[1:])

for inst in open(input):
    if inst[0] in ['L', 'R']:
        dir=changedir(dir, inst) 
    else:
        move(dir,inst,pos)
    
print(abs(pos[0]) + abs(pos[1]))