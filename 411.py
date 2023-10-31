def sqr_xz(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return [-1]
    if a == 0 and b == 0:
        return [0]
    if a == 0:
        return [1, -c/b]
    d = b**2 - (4*a*c)
    if d < 0:
        return [0]
    if d == 0:
        return [1, -b/(a*2)]
    if d > 0:
        x1 = (-b + (d**0.5)) / (a*2)
        x2 = (-b - (d**0.5)) / (a*2)
        return [2, x1, x2]

a, b, c = map(int, input().split())
result = sqr_xz(a, b, c)

for i in result:
    print(i)
