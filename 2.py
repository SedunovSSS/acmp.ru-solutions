n = int(input())
result = 0
if n > 0:
    for i in range(1, n+1):
        result += i
else:
    for i in range(1, n-1, -1):
        result += i

print(result)