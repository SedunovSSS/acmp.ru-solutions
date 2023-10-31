n = int(input())
roads = [list(map(int, input().split())) for _ in range(n)]
x = sum([sum(i) for i in roads])//2
print(x)
