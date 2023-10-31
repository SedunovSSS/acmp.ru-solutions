n = int(input())
d = {i:7-i for i in range(6) if i != 0}
d[0] = 0
print(n // 6 + d[n % 6], n*6)