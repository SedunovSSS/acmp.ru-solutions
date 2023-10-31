def s(n):
    return str(bin(n)).count('1')

n = int(input())
print(n+s(n))