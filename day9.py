import time

t1 = time.perf_counter()
src = open('input9.txt', 'r')
inp = src.readlines()
# creating list preamb with first 25 numbers and nextval with other ones
preamb = []
nextval = []
for x in range(len(inp)):
    if x < 25:
        preamb.append(int(inp[x]))
    else:
        nextval.append(int(inp[x]))

# creating summatrix where all curent sums are stored in nested list
summatrix = []
for x in range(len(preamb)):
    a = []
    for y in range(x):
        a.append(preamb[x] + preamb[y])
    summatrix.append(a)
''' I'll come back for you
# creating vect with new sums, updating preamb and summatrix
print(nextval)
for x in range(len(nextval)):
    #if not any(nextval[x] in z for z in summatrix):
     #   print(nextval[x])
      #  break
    n = x % 25
    vect = []
    preamb.pop(n)
    for a in preamb[:-1]:
        vect.append(a + nextval[x])
    preamb.insert(n,nextval[x])
    # horizontal list
    summatrix[n] = vect[:n+1]
    # vertical list
    for y in range(n+1, len(vect)):
        summatrix[y+1][n+1] = vect[y]
    print(vect)
'''
for z in nextval:
    if not any(z in d for d in summatrix):
        weakness=z
        print(weakness)
        break
    summatrix=[]
    preamb.pop(0)
    preamb.append(z)
    for x in range(len(preamb)):
        a = []
        for y in range(x):
            a.append(preamb[x] + preamb[y])
        summatrix.append(a)
#part two
for x in range(len(nextval)):
    check=nextval[x]
    n=1
    res=[nextval[x]]
    while check < weakness:
        check+=nextval[x+n]
        res.append(nextval[x + n])
        n+=1
    else:
        if check==weakness:
            print(min(res)+max(res))
            break
t2=time.perf_counter()
print(t2-t1)