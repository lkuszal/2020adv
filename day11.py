import numpy as np

src = open('input11.txt', 'r')
inp = src.readlines()
b = []
for inpx in inp:
    a = []
    for inpy in inpx[:-1]:
        a.append(inpy)
    b.append(a)
seats = np.array(b)
yn = len(seats)
xn = len(seats[0])
floorrow = [["."] * xn]
floorcol = ["."] * (yn + 2)
seats = np.concatenate((floorrow, seats, floorrow))
seats = np.c_[floorcol, seats, floorcol]
seatsclean = seats.copy()


def sitting():
    global seats, seats2
    seats2 = seats.copy()
    for y in range(1, yn + 1):
        for x in range(1, xn + 1):
            if seats[y][x] == "L":
                if not (seats[y - 1][x - 1], seats[y - 1][x], seats[y - 1][x + 1], seats[y][x - 1], seats[y][x + 1],
                        seats[y + 1][x - 1], seats[y + 1][x], seats[y + 1][x + 1]).count("#"):
                    seats2[y][x] = "#"


def unsitting():
    global seats, seats2
    seats = seats2.copy()
    for y in range(1, yn + 1):
        for x in range(1, xn + 1):
            if seats2[y][x] == "#":
                if 3 < (
                        seats2[y - 1][x - 1], seats2[y - 1][x], seats2[y - 1][x + 1], seats2[y][x - 1],
                        seats2[y][x + 1],
                        seats2[y + 1][x - 1], seats2[y + 1][x], seats2[y + 1][x + 1]).count("#"):
                    seats[y][x] = "L"


a = len(np.where(seats == "L")[0])
b = 0
while b - a:
    a = b
    sitting()
    unsitting()
    b = len(np.where(seats == "#")[0])
print(b)
# part two
seats = seatsclean.copy()
cord = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def sight(y, x, mapver):
    sightres = []
    for direct in cord:
        n = 1
        cury = y + direct[0] * n
        curx = x + direct[1] * n
        while cury in range(yn + 2) and curx in range(xn + 2):
            if mapver[cury][curx] != ".":
                sightres.append(mapver[cury][curx])
                break
            else:
                n += 1
                cury = y + direct[0] * n
                curx = x + direct[1] * n
        else:
            sightres.append(".")
    return sightres


def sitting2():
    global seats, seats2
    seats2 = seats.copy()
    for y in range(1, yn + 1):
        for x in range(1, xn + 1):
            if seats[y][x] == "L":
                if "#" not in sight(y, x, seats):
                    seats2[y][x] = "#"


def unsitting2():
    global seats, seats2
    seats = seats2.copy()
    for y in range(1, yn + 1):
        for x in range(1, xn + 1):
            if seats2[y][x] == "#":
                if sight(y, x, seats2).count("#") > 4:
                    seats[y][x] = "L"


a = len(np.where(seats2 == "L")[0])
b = 0
while b - a:
    a = b
    sitting2()
    unsitting2()
    b = len(np.where(seats == "#")[0])
    print(b)
