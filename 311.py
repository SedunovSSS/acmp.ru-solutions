from math import factorial
n = int(input())
print(sum([factorial(i) for i in range(1, n+1)]))
