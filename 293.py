n = int(input())
a = [list(map(int, input().split())) for _ in range(2)]

max_nalog = float('-inf')
number = 0

for i in range(n):
    dohodi = a[0][i]
    nalogi = a[1][i]
    sum_nalog = (dohodi / 100) * nalogi
    if sum_nalog > max_nalog:
        max_nalog = sum_nalog
        number = i+1

print(number)