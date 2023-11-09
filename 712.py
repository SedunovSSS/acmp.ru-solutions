w, h, n = map(int, input().split())
x = 0
m = float('inf')

while x**2 < n:
    x += 1
    y = (n-1) // x+1
    m = min(m, max(w*x, y*h), max(w*y, h*x))

print(m)
