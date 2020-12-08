src = open('input8.txt', 'r')
inp = src.read()
inp = inp.split("\n")
'''
executed=[]
line=0
acc=0
while line not in executed:
    executed.append(line)
    inst=inp[line]
    if inst[:3] == "acc":
        acc+=int(inst[4:])
        line+=1
    elif inst[:3] == "jmp":
        line+=int(inst[4:])
    else:
        line+=1
print(acc)
'''
#part two
for x in range(len(inp)):
    newinp=inp[:]
    newinst=newinp[x]
    if newinst[:3]!="acc":
        if newinst[:3]=="jmp":
            newinst="nop"+newinst[3:]
            newinp[x]=newinst
        elif newinst[:3]=="nop":
            newinst="jmp"+newinst[3:]
            newinp[x]=newinst
        executed=[]
        line=0
        acc=0
        try:
            while line not in executed:
                executed.append(line)
                inst=newinp[line]
                if inst[:3] == "acc":
                    acc+=int(inst[4:])
                    line+=1
                elif inst[:3] == "jmp":
                    line+=int(inst[4:])
                else:
                    line+=1
        except IndexError:
            print(acc)
            break