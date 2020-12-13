src = open('input130.txt', 'r').read().split("\n")
curtime = int(src[0])
bustimes = src[1].split(",")
bustimes = set(bustimes)
try:
    bustimes.remove("x")
except KeyError:
    pass
bustimes = list(map(int, bustimes))


def timepass(time):
    while True:
        for bus in bustimes:
            if time % bus == 0:
                return ((time - curtime) * bus)
        time += 1


print(timepass(curtime))

# part two
busdif = src[1].split(",")
busdict = {}
n = 0
for x in busdif:
    if x != "x":
        busdict[n] = int(x)
    n += 1

print(busdict)


def redicting(inpdict):
    highestvalue = (max(inpdict.values()))
    for x in inpdict.keys():
        if inpdict[x] == highestvalue:
            highkey = x
            break
    newdict = {}
    for x in inpdict.keys():
        newdict[x - highkey] = inpdict[x]
    return newdict, highestvalue, highkey


def timejumper(inpdict, val, key):
    time = 0
    while True:
        for x in inpdict.keys():
            if not (time + x) % inpdict[x] == 0:
                break
        else:
            return time - key
        time += val


a = list(busdict.keys())
dif0 = a[0]
mult0 = busdict[dif0]
'''
for y in a[1:]:
    dif1=y
    mult1=busdict[y]
    dif0=0
    dif1-=dif0
    time=0
    print(dif0,mult0,dif1,mult1)
    while True:
        time+=mult0
        if time+dif1==mult1:
            mult0=time
            dif0=dif1
            break'''

newdict, val, key = redicting(busdict)
print(timejumper(newdict, val, key))
