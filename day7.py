src = open('input7.txt', 'r')
inp = src.read()[:-1]
inp = inp.split("\n")
bags={}
bags2={}
for x in inp:
    x = x.split(" ")
    a=[]
    b=[]
    z = 0
    for n in range(len(x)):
        if "bag" in x[n]:
            a.append(x[n-2] + " " + x[n-1])
            if z == 0:
                b.append(x[n-2] + " " + x[n-1])
                z = 1
            else:
                if "other" != x[n-1]:
                    b.append([int(x[n-3]), x[n-2] + " " + x[n-1]])
    bags.update({a[0]:a[1:]})
    bags2.update({b[0]:b[1:]})
#part1
n=0
results=["shiny gold"]
while len(results) != n:
    n = len(results)
    for bag in results:
        for x in bags.keys():
            if bag in bags[x]:
                if x not in results:
                    results.append(x)
print(n-1)
#part2
results2=[[1, "shiny gold"]]
n=0
while results2:
    x=results2[0]
    a=bags2[x[1]]
    for y in a:
        results2.append([y[0]*x[0],y[1]])
    n += x[0]
    results2.pop(0)
    print(n,results2)
print(n-1)

