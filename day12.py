src = open('input12.txt', 'r')
inp = src.readlines()
inplist=[]
for x in inp:
    inplist.append(x[:-1])
dirdict={"N":(0,1),"E":(1,0),"S":(0,-1),"W":(-1,0)}
ddkeys=dirdict.keys()
posx=0
posy=0
direction=90
rotation={0:"N",90:"E",180:"S",270:"W"}
for x in inplist:
    z=x[0]
    if z in ddkeys:
        posx+=dirdict[z][0]*int(x[1:])
        posy+=dirdict[z][1]*int(x[1:])
    elif z == "R":
        direction+=int(x[1:])
    elif z == "L":
        direction-=int(x[1:])
    elif z == "F":
        posx+=dirdict[rotation[direction%360]][0]*int(x[1:])
        posy+=dirdict[rotation[direction%360]][1]*int(x[1:])
print(abs(posx)+abs(posy))
#part two
