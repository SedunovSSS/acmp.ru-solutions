x1, y1, x2, y2 = map(int, input().split())
x, y = map(int, input().split())
print(2*x1-x, y) if x1 == x2 else print(x, 2*y1 - y)