src=open('input4.txt','r')
a=src.read()
b=a.split("\n\n")
n1=0
n2=0
req=set(['byr', 'iyr', 'eyr', 'ecl', 'pid', 'hcl', 'hgt'])
eye=["amb","blu","brn","gry","grn","hzl", "oth"]
for x in b:
    x=x.replace("\n"," ")
    x=x.split()
    c={}
    for y in x:
        y=y.split(':')
        c.update({y[0]: y[1]})
    if req.issubset(set(c)):
        n1+=1
    for y in x:
        y=y.split(':')
        c.update({y[0]: y[1]})
    try:
        if (int(c["byr"]) in range(1920,2003)) and (int(c["iyr"]) in range(2010,2021)) and (int(c["eyr"]) in range(2020,2031)) and ((c["hgt"][-2:]=="cm" and int(c["hgt"][:3]) in range(150,194)) or (c["hgt"][-2:]=='in' and int(c["hgt"][:2]) in range(59,77))) and (c["ecl"] in eye) and len(c["pid"])==9 and int(c["pid"]) and c["hcl"][0]=='#' and len(c["hcl"])==7 and int(c["hcl"][1:],16):
            n2+=1
    except KeyError: pass
    except ValueError: pass
print(n1,n2)