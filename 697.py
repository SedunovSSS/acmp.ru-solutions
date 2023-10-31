def ceil(flnum):
    if flnum > int(flnum):
        return int(flnum)+1
    return int(flnum)


l, w, h = map(int, input().split())
S = 2*(w*h+l*h) / 16
S = ceil(S)
print(S)
