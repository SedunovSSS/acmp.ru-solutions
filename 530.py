def get(a, b, key):
    if a==b=='0':
        return key[0]
    if a=='0' and b == '1':
        return key[1]
    if a=='1' and b == '0':
        return key[2]
    if a==b=='1':
        return key[3]


w, h = map(int, input().split())
matrix1 = [input() for _ in range(h)]
matrix2 = [input() for _ in range(h)]
key = input()

result = ''

for i in range(h):
    for j in range(w):
        a, b = matrix1[i][j], matrix2[i][j]
        result += get(a, b, key)
    result += '\n'

print(result)

