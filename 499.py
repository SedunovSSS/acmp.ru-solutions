k, w = map(int, input().split())
a1, b1, a2, b2, a3, b3 = map(int, input().split())

count = 0

if a1 <= w and b1 >= k:
    count += 1
if a2 <= w and b2 >= k:
    count += 1
if a3 <= w and b3 >= k:
    count += 1
if a1 + a2 <= w and b1 + b2 >= k:
    count += 1
if a1 + a3 <= w and b1 + b3 >= k:
    count += 1
if a2 + a3 <= w and b2 + b3 >= k:
    count += 1
if a1 + a2 + a3 <= w and b1 + b2 + b3 >= k:
    count += 1

if count > 0:
    print("YES")
else:
    print("NO")
