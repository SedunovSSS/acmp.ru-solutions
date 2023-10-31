a, b, n = map(int, input().split())
d = b-a

result = a

for i in range(n-1):
    result += d

print(result)
