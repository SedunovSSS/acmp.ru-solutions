m = [['B' if (i+j)%2 == 0 else 'W' for j in range(8)] for i in range(8)]
x1, y1, x2, y2 = map(int, input().split())
print('YES' if m[x1-1][y1-1] == m[x2-1][y2-1] else 'NO') 