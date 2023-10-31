a = int(input())
ns_and_ms = [[int(j) for j in input().split()]for _ in range(a)]
ds = []

for i in ns_and_ms:
    n, m = i[0], i[1]
    d = 19*m + (n + 239)*(n + 366)/2
    ds.append(d)

for i in ds:
    print(int(i))
