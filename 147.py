def check(n):
    prev = 0
    curr = 1

    if n == 0: return 0

    for _ in range(1, n):
        next = prev + curr
        prev = curr
        curr = next

    return curr
    

n = int(input())
print(check(n))