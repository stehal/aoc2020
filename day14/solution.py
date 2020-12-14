input='input'

mem = {}
for s in open(input):
    if s[:4] == "mask":
        m = s.split("=")[1].strip()
        m_0 = int(m.replace("X", '0'),2)
        m_1 = int(m.replace('X', '1'),2)
    else:
        mm = s.split("=")
        adr = int(mm[0].replace("mem[", '').replace(']',''))
        mem[adr] =  (int(mm[1])|m_0)&(int(mm[1])|m_1)
        
print(sum(mem.values()))