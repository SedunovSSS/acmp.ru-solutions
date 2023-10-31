n, m = map(int, input().split())
if n % m == 0:
    print(*[n // m for _ in range(m)])
else:
    a = n // m
    b = [a for _ in range(m)]
    c = n % m
    for i in range(m-c, m):
        b[i] = b[i] + 1
    print(*b)