n, m = map(int, input().split())
screensaver = [input() for _ in range(n)]
tablo = [list(map(int, input().split())) for _ in range(n)]
colors = {0:'.',1:'.B',2:'.G',3:'.GB',4:'.R',5:'.RB',6:'.RG',7:'.RGB'}

for i in range(n):
    for j in range(m):
        color = colors[tablo[i][j]]
        if screensaver[i][j] not in color:
            print('NO')
            break
    else:
        continue
    break
else:
    print('YES')
