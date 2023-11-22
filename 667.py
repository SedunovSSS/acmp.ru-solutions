n, m, k = map(int, input().split())
ceil = lambda x: int(x) if x == int(x) else int(x) + 1
buses = ceil((n+m)/k)
if m * (k-2) < n*2:
    print(0)
else:
    print(buses)
