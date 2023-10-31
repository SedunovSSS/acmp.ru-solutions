a, b, c, d = map(int, input().split())
horny = []

for x in range(-100, 101):
    if a*x**3 + b*x**2 + c*x + d == 0:
        horny.append(x)

horny = list(sorted(list(set(horny))))
print(*horny)