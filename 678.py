commands = list(input())

glist = [1, 0, 0]

for i in commands:
    if i == 'A':
        glist[0], glist[1] = glist[1], glist[0]
    if i == 'B':
        glist[2], glist[1] = glist[1], glist[2]
    if i == 'C':
        glist[2], glist[0] = glist[0], glist[2]

print(glist.index(1) + 1)
