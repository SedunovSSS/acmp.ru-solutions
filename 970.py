def check(a, b, c):
    if a + b == c:
        return 'YES'
    if a + c == b:
        return 'YES'
    if b + c == a:
        return 'YES'
    return 'NO'


a, b, c = map(int, input().split())
print(check(a, b, c))
