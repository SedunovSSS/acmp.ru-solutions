n, m = map(int, input().split())
_map = [input() for _ in range(n)]
min_dist = m
for i in _map: min_dist = min(min_dist, i.count('.'))
print(min_dist)
