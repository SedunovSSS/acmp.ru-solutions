a = int(input())
glist_map = map(int, input().split())
glist = []
summa = 0
proizv = 1
b = 1

for i in glist_map:
    glist.append(int(i))

for i in glist:
    if i >= 0:
        summa += i

x_min, x_max = min(glist), max(glist)
if glist.index(x_min) >= glist.index(x_max):
    b = -1
else:
    b = 1

for i in range(glist.index(x_min)+b, glist.index(x_max), b):
    proizv *= glist[i]

print(summa, proizv)