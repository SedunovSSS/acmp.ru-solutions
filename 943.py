n, m, y, x = map(int, input().split())
matrix = [list(range(i, i+m)) if i//m % 2 == 0 else list(range(i+m-1, i-1, -1)) for i in range(0, n*m, m)]
print(matrix[y-1][x-1])