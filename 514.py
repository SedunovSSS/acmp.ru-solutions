def find_last_step(K):
    height = 0
    i = 1
    while K >= i:
        height += 1
        K -= i
        i += 1
    return height

k = int(input())
result = find_last_step(k)
print(result)