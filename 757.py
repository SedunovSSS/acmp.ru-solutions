glist = list(map(int, input().split()))
c2h5oh = [2, 6, 1]
glist1 = []

for i in range(len(glist)):
    glist1.append(glist[i] // c2h5oh[i])

print(min(glist1))
