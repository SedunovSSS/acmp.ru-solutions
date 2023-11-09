n, m = map(int, input().split())
map_ = [input() for _ in range(n)]
_map_ = [['.'] * (m+2) for _ in range(n+2)]

for i in range(1, n+1):
    for j in range(1, m+1):
        _map_[i][j] = map_[i-1][j-1]

count = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if _map_[i][j] != '*':
            for row in [-1, 0, 1]:
                for col in [-1, 0, 1]:
                    if row == 0 and col in [1, -1] or col == 0 and row in [1, -1]:
                        so_sed = _map_[i+row][j+col]
                        if so_sed == '*':
                            break
                else:
                    continue
                break
            else:
                count += 1

print(count)
