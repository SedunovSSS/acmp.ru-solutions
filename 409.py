n = int(input())
line = list(map(int, input().split()))
a = []
for i in range(n):
    a.append(int(line[i]))
b = []
for i in range(n - 1):
    b.append((a[i] + a[i + 1]) / 2)
ans = sum(b) / len(b)
ans = '%.10f' % ans
print(ans)
