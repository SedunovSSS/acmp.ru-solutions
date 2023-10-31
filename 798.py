m, n, i, j, c = map(int, input().split())
if m * n % 2 == 0:
    print("equal")
else:
    color = ((i + j) % 2) ^ c
    print('white' if color == 1 else 'black')
