a, b, k = map(int, input().split())

i = 0

while i < k:
    a = 10*(a % b)
    i+=1

print(a//b)
