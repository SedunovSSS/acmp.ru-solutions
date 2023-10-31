def check(n, m, k):
    if n >= m:
        count = 1
    else:
        if n <= k:
            count = "NO"
        else:
            w = n - k
            q = (m - n - 1) // w
            count = q + 2
            
    return count
    


n, m, k = map(int, input().split())
print(check(n, m, k))