tr, tc = map(int, input().split())
mode = input()
ans = 0

if mode == "freeze":
    if tr < tc:
        ans = tr
    else:
        ans = tc
if mode == "heat":
    if tr < tc:
        ans = tc
    else:
        ans = tr
if mode == "auto":
    ans = tc
if mode == "fan":
    ans = tr

print(ans)
