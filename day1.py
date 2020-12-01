src=open("C:/Users/Latul/Desktop/input.txt","r")
a=[]
for x in src.readlines():
    a.append(int(x[:-1]))
for x in range(len(a)):
    for y in range(x+1,len(a)):
        for z in range(y+1,len(a)):
            if a[x]+a[y]+a[z]==2020:
                print(a[x],a[y],a[z],a[x]*a[y]*a[z])