n = int(input())
vals = list(map(int, input().split()))
m = int(input())
cords = [list(map(int, input().split())) for _ in range(m)]
[print(*vals[f-1:s]) for f, s in cords]