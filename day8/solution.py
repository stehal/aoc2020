infile = "input"

prog = [s.strip().split() for s in open(infile)]

visited = set()

def run(pointer, acc):
    if pointer in visited:
        return acc
    visited.add(pointer)
    if prog[pointer][0] == 'nop':
        pointer +=1
    if prog[pointer][0] == 'acc':
        acc +=int(prog[pointer][1])
        pointer +=1
    if prog[pointer][0] == 'jmp':
        pointer +=int(prog[pointer][1])
    return run(pointer, acc)   
    
print(run(0, 0))
 


