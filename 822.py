x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))
a = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
b = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
c = ((x2 - x3) ** 2 + (y2 - y3) ** 2) ** 0.5
p = (a + b + c) / 2
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(round(s, 2))