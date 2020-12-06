src = open('input6.txt', 'r')
inp = src.read()
inp = inp[:-1].split("\n\n")
sets = []
p2inp = []
for x in inp:
    sets.append(set(x.replace("\n", "")))
    p2inp.append(x.split("\n"))
part1 = 0
for x in sets:
    part1 += len(x)
print(part1)
# part two
part2 = 0
for group in p2inp:
    for char in group[0]:
        ind = True
        for person in group:
            if char not in person:
                ind = False
        if ind:
            part2 += 1
print(part2)
