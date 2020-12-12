input = "input"
pos = [0,0]
wp = [1, 10]
dir = 1 #e
compass =  ['N', 'E', 'S', 'W']
dirs = [(1,0), (0,1), (-1,0), (0, -1)] #n,e,s,w

def rotate(wp, inst):
    turns = int(inst[1:])
    if inst[0] == 'L':
        turns = 360 - turns
    for i in range(turns/90 % 4):
        wp = [-wp[1], wp[0]]
    return wp
    
def movesh(pos, wp, inst):
    pos[0]+=wp[0]*int(inst[1:])
    pos[1]+=wp[1]*int(inst[1:])
    
def movewp(inst, pos):
    move_dir = dirs[compass.index(inst[0])]
    pos[0]+=move_dir[0]*int(inst[1:])
    pos[1]+=move_dir[1]*int(inst[1:])

for inst in open(input):
    if inst[0] in ['L', 'R']:
        wp = rotate(wp, inst)
    elif inst[0] in compass:
        movewp(inst,wp)
    else:
        movesh(pos, wp, inst)
    
print(abs(pos[0]) + abs(pos[1]))


