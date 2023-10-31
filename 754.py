glist = map(int, input().split())
glist1 = []
for i in glist:
    glist1.append(int(i))

if min(glist1) <= 93 or max(glist1) > 727:
    print("Error")
else:
    print(max(glist1))
