n = int(input())
graduses = list(map(int, input().split()))
_len = 0
_max_len = _len

for i in range(n):
    for j in range(i+1, n+1):
        sub_list = graduses[i:j]
        for k in sub_list:
            if k <= 0:
                _len = 0
                break
        else:
            _len = len(sub_list)
        _max_len = max(_len, _max_len)
        
print(_max_len)
