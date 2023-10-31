string = input()
floor = 0
mxf = 0
mnf = 0

for i in string:
    if i == '1':
        floor += 1
    else:
        floor -= 1

    mxf = max(floor, mxf)
    mnf = min(floor, mnf)

print(mxf-mnf+1)
