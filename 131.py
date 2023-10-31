n = int(input())
vals = [list(map(int, input().split())) for _ in range(n)]

result = -1
year = 0

for y, g in vals:
    if g == 1 and year < y:
        year = y
        result = vals.index([y, g]) + 1

print(result)
