n, m = map(int, input().split())
first = [input() for _ in range(n)]
input()
second = [input() for _ in range(n)]

count = 0
moved = []

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(n):
    for j in range(m):
        if first[i][j] != '.' and second[i][j] != first[i][j]:
            count += 1
            moved.append(first[i][j])

moved.sort(key=ascii_letters.index)

print(count)
print(*moved, sep='')
