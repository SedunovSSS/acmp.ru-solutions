a, b, c = map(int, input().split())

S = 2 * (a * b + a * c + b * c)
V = a*b*c

print(S, V)