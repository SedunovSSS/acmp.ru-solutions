n, k = map(int, input().split())
b = ''
while n > 0:
    b = str(n % k) + b
    n = n // k
 
_sum = sum(map(int, b))
multiply = 1
 
for i in b:
    multiply *= int(i)
 
print(multiply-_sum)