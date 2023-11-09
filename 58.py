t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    if n < 2 or m < 2:
        results.append('YES')
        continue
    for i in range(n - 1):
        for j in range(m - 1):
            submatrix = []
            for k in range(2):
                submatrix += table[i+k][j:j+2]
            if len(set(submatrix)) == 1:
                results.append('NO')
                break
        else:
            continue
        break
    else:                            
        results.append('YES')    

print(*results, sep='\n')
