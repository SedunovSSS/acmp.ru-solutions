n, m, k = map(int, input().split())
map_ = [input() for _ in range(n)]

for kk in range(k):
    map__ = []
    for i in range(n):
        newstr = ''
        for j in range(m):
            s = map_[i-1][j-1] + map_[i-1][j] + map_[i-1][(j+1)%m]
            s += map_[i][j-1] + map_[i][(j+1)%m]
            s += map_[(i+1)%n][j-1] + map_[(i+1)%n][j] + map_[(i+1)%n][(j+1)%m]
            cnt = s.count('*')
            if map_[i][j] == "*":
                newstr += "*" if 1 < cnt < 4 else '.'
            else:
                newstr += "*" if cnt == 3 else '.'
            
        map__.append(newstr) 
    map_ = map__.copy()


for i in map_:
    print(i)
