a, b = map(int, input().split())
x = (a*b)**0.5
print(int(x) if x == int(x) else 0)