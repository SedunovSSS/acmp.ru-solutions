sysx, sysy = map(int, input().split())
dogx, dogy = map(int, input().split())

cords = [list(map(int, input().split())) for _ in range(int(input()))]

vals = []

for index, (x, y) in enumerate(cords):
    len_sys = ((sysx-x) ** 2 + (sysy-y) ** 2) ** 0.5
    len_dog = ((dogx-x) ** 2 + (dogy-y) ** 2) ** 0.5

    if 2*len_sys <= len_dog:
        vals.append(index+1)

print('NO' if len(vals) == 0 else vals[0])
