s, r1 = map(float, input().split())
pi = 3.141592653589793
s1 = pi * (r1 ** 2)
s2 = s1 - s
r2 = (s2 / pi) ** 0.5
print(round(r2, 3))