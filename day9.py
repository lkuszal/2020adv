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

# creating vect with new sums, updating preamb and summatrix
print(nextval)
for x in range(len(nextval)):
    if not any(nextval[x] in z for z in summatrix):
        print(nextval[x])
        break
    n = x % 24
    vect = []
    preamb.pop(0)
    preamb.append(nextval[x])
    for a in preamb[:-1]:
        vect.append(a + nextval[x])
    # horizontal list
    summatrix[n+1] = vect[:n+1]
    # vertical list
    for y in range(n+1, len(vect)):
        summatrix[y+1][n+1] = vect[y]

