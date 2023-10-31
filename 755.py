x, y, z = map(int, input().split())
print('Impossible' if (x + y - z) < 0 else (x + y - z))