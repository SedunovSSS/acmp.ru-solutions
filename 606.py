a, b, c = map(int, input().split())

if max(a, b, c) == a:
    if a < b+c:
        print("YES")
    else:
        print("NO")

elif max(a, b, c) == b:
    if b < a+c:
        print("YES")
    else:
        print("NO")

elif max(a, b, c) == c:
    if c < a+b:
        print("YES")
    else:
        print("NO")
