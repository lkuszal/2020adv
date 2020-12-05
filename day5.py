src=open("input5.txt","r")
results=[]
results2=[]
ys=[]
xs=[]
for seat in src.readlines():
    seat=seat.replace("F","0")
    seat=seat.replace("B", "1")
    seat=seat.replace("L", "0")
    seat=seat.replace("R", "1")
    y=int(seat[:7],2)
    x=int(seat[-4:-1],2)
    results.append(y*8+x)
    results2.append([x,y])
    xs.append(x)
    ys.append(y)
print(max(results))
xs=range(min(xs),max(xs)+1)
ys=range(min(ys)+1,max(ys))
for x in xs:
    for y in ys:
        if [x,y] not in results2:
            print(y*8+x)
