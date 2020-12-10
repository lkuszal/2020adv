src = open('input10.txt', 'r')
inp = src.readlines()
adapters=[]
for x in inp:
    adapters.append(int(x))
adapters.sort()
diff={1:0,2:0,3:1}
prev=0
for x in adapters:
    if x-prev in range(1,4):
        diff[x-prev]+=1
        prev=x
print(diff[1]*diff[3])
#part two
adapters.insert(0,0)
a=''
for x in range(1,len(adapters)):
    a+=str(adapters[x]-adapters[x-1])
b=a.split("3")
res=1
for x in b:
    if len(x) == 2: res = res * 2
    if len(x) == 3: res = res * 4
    if len(x) == 4: res = res * 7
print(res)