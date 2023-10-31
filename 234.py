n, m, k = map(int, input().split())
cord_mines = [list(map(int, input().split())) for _ in range(k)]
map_ = [[0] * (m+2) for _ in range(n+2)]

for i in range(0, k):
    map_[cord_mines[i][0]][cord_mines[i][1]] = '*'

for i in range(1, n+1):
    for j in range(1, m+1):
        count = 0
        if map_[i][j] != '*':
            for row in [-1, 0, 1]:
                for col in [-1, 0, 1]:
                    so_sed = map_[i+row][j+col]
                    if so_sed == '*':
                        count += 1

            map_[i][j] = count

new_map = []
for i in range(1, n+1):
    temp = []
    for j in range(1, m+1):
        if map_[i][j] == 0:
            temp.append('.')
        else:
            temp.append(str(map_[i][j]))
    new_map.append(temp)

[print(''.join(i)) for i in new_map]