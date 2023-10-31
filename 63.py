s, p = map(int, input().split())

for x in range(1, 1001):
    for y in range(1, 1001):
        if x+y == s and x*y == p:
            print(x, y)
            break
    else:
        continue
    break