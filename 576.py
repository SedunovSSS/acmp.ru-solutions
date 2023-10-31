from math import gcd

n = int(input())
xz = n
result = 0

while True:
    xz -= 1
    if xz == 0: break
    if gcd(xz, n) == 1: result += 1
    
print(result)