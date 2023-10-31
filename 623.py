def check(n):
    curr = prev = 1
    for _ in range(n-1):
        curr, prev = (curr+prev)%10, curr
    return curr
    

n = int(input())
print(check(n))
