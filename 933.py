a, b, c, t = map(int, input().split())
print(t*b if a >= t else (t - a) * c + a * b)