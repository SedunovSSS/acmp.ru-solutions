a, b = map(int, input().split())
drivers = []
numbers = []
sums = []

for i in range(a):
    drivers.append(input())
    numbers.append(list(map(int, input().split())))

for i in range(a):
    sums.append(sum(numbers[i]))

print(drivers[sums.index(min(sums))])