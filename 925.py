k = int(input())
n, a, b, c = map(int, input().split())

if k == 2:
    print(min(a, b, c))
else:
    print(max(a + b + c - 2 * n, 0))
