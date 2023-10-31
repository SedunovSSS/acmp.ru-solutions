n = int(input())
l, r = 32, 0
for i in range(n):
    a, b = map(int, input().split())
    l = min(b, l)
    r = max(a, r)

print('NO' if r > l else 'YES')
