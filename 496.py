n = int(input())
values = list(map(int, input().split()))

sums = []

for i in range(0, n):
    if i == 0:
        sums.append(sum([values[i], values[i+1], values[-1]]))
    elif i == n-1:
        sums.append(sum([values[i-1], values[i], values[0]]))
    else:
        sums.append(sum([values[i-1], values[i], values[i+1]]))

print(max(sums))
