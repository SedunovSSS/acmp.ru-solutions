a, b = map(int, input().split())
count = 0
for i in range(a, b + 1):
    n = str(i)
    pr = 1
    for j in range(len(n)):
        pr = pr * int(n[j])
    if pr != 0:
        if i % pr == 0:
            count += 1
print(count)
