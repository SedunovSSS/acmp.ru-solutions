glist = list(map(int, input().split()))

if glist[0] >= glist[1] + glist[-1]:
    print("YES")
else:
    print("NO")
