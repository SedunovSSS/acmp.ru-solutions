from math import factorial, ceil
n = int(input())
print(sum([ceil(factorial(n)/(factorial(n-i)*factorial(i))) for i in range(2, n+1)]))