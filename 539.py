def check(n):
    if n % 2 == 0 :
        return n // 2
    elif n == 1:
        return 0
    else:
        return n
    
n = int(input())
print(check(n))
