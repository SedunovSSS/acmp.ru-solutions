n, an, an1 = map(int, input().split())

for i in range(n-1): 
    an, an1 = an1-an, an

print(an, an1)