n, m = map(int, input().split())
table = [[i*j for j in range(1, m+1)] for i in range(1, n+1)]

red, green, blue, black = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if table[i][j] % 5 == 0:
            blue += 1
        elif table[i][j] % 3 == 0:
            green += 1
        elif table[i][j] % 5 == 0:
            blue += 1
        elif table[i][j] % 2 == 0:
            red += 1
        else:
            black += 1

print(f'RED : {red}')
print(f'GREEN : {green}')
print(f'BLUE : {blue}')
print(f'BLACK : {black}')