def check(n):
    prev = 0
    curr = 1
    fibs = [curr]
    while curr < n:
        next = prev + curr
        prev = curr
        curr = next
        fibs.append(curr)

    return [1, fibs.index(n)+1] if n in fibs else [0]
    

n = int(input())
print(*check(n), sep='\n')
