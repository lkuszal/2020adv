src=open("input3.txt","r")
road=[]
for x in src.readlines():
    a=[]
    for y in x[:-1]:
        if y==".":
            a.append(0)
        else: a.append(1)
    road.append(a)
trees=0
width=len(road[0])
def treescounter(a,b):
    trees=0
    for y in range(len(road)//b):
        x = (a * y) % width
        yn=(b * y)
        trees += road[yn][x]
    return trees
print(treescounter(3,1))
print(treescounter(1,1)*treescounter(3,1)*treescounter(5,1)*treescounter(7,1)*treescounter(1,2))