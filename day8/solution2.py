import copy
infile = "input"

visited = set()

def run(prg, pointer, acc):
    if pointer >= len(prg):
        return acc, True
    if pointer in visited:
        return acc, False
    visited.add(pointer)
    if prg[pointer][0] == 'nop':
        pointer +=1
    if prg[pointer][0] == 'acc':
        acc +=int(prg[pointer][1])
        pointer +=1
    if prg[pointer][0] == 'jmp':
        pointer +=int(prg[pointer][1])
    return run(prg, pointer, acc)   
    
prog = [ s.strip().split() for s in open(infile)]

for i in range(0,len(prog)):
    visited = set()
    prg = copy.deepcopy(prog)
    s = prog[i][0]
    if s == 'nop':
       prg[i][0] ='jmp' 
    if s == 'jmp':
       prg[i][0] ='nop' 
    r = run(prg, 0, 0)
    if r[1]:
        print(r[0])
        break
 


