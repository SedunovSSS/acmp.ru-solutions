n = int(input())
for i in range(n, -1, -1):
    xz = 5*i
    if xz > n:
        continue
    k = n - xz
    if k % 3 != 0:
        continue
    print(i, k//3)
    break