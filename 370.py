n = int(input())
cords = [list(map(int, input().split())) for _ in range(n)]

_sum = 0

for i in range(n):
    xi, yi = cords[i][0], cords[i][1]
    if i == n-1:
        i = -1
    xi1, yi1 = cords[i+1][0], cords[i+1][1]
    _sum += (xi1-xi)*(yi1+yi)

_sum = abs(_sum)

print(0.5*_sum)
