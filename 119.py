n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times = [i[0]*3600+i[1]*60+i[2] for i in times]
times.sort()

for i in times:
    h = i // 3600
    m = (i-h*3600)//60
    s = i-(h*3600)-(m*60)
    print(h, m, s)
