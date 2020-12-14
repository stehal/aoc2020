input='input'

mem = {}

def ones(adr, mask):
    new_adr= []
    for a, m in zip(adr,mask) :
        if m == '1':
            new_adr.append('1')
        else:
            new_adr.append(a)
    return ''.join(new_adr)

def all_adr(start, mask, adr ,all):
    for i, x in enumerate(mask[start:]):
        if (x== 'X'):
            adr0 = adr[: i +start] + '0' + adr[i + start +1:]
            adr1 = adr[: i +start] + '1' + adr[i+start+1:]
            all.add(adr0)
            all.add(adr1)
            all_adr(i +start +1,mask, adr0, all)
            all_adr(i +start +1,mask, adr1, all)

for s in open(input):
    if s[:4] == "mask":
        mask = s.split("=")[1].strip()
    else:
        mm = s.split("=")
        adr = "{:036b}".format(int(mm[0].replace("mem[", '').replace(']','')))
        val =   int(mm[1])
        all = set()
        all_adr(0,mask,ones(adr, mask), all )
        for a in all:
            mem[int(a, 2)] = val

print(sum(mem.values()))

        

