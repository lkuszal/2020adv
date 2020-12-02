import re
src=open("input2.txt","r")
a=[]
for x in src.readlines():
    x=re.split("-| |: ", x[:-1])
    a.append(x)
#part1
c=0
for x in a:
    z = x[3].count(x[2])
    if z>=int(x[0]) and z<=int(x[1]):
        c+=1
print(c)
#part2
d=0
for x in a:
    if ((x[3][int(x[0])-1]==x[2]) != (x[3][int(x[1])-1]==x[2])):
        d+=1
print(d)