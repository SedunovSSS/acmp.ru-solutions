glist = list(map(int, input().split()))
minn, maxx = [], []
for i in range(len(glist)):
    if i % 2 == 0:
        minn.append(glist[i])
    else:
        maxx.append(glist[i])

print(min(minn)+max(maxx))