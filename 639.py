n = int(input())

def check(a, b):
    ascii_letters = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l = min(len(a), len(b))
    for i in range(l):
        if ascii_letters.index(a[i]) < ascii_letters.index(b[i]):
            return False
        if ascii_letters.index(a[i]) > ascii_letters.index(b[i]):
            return True
    return False if l == len(a) else True


units = []

for _ in range(n):
    m = int(input())
    for _ in range(m):
        score, name = input().split()
        score = float(score)
        units.append([score, name])

_len = len(units)

for i in range(_len-1):
    for j in range(_len-i-1):
        if units[j][0] < units[j+1][0]:
            units[j], units[j+1] = units[j+1], units[j]
        if units[j][0] == units[j+1][0] and check(units[j][1], units[j+1][1]):
            units[j], units[j+1] = units[j+1], units[j]

print(_len)
for i in units:
    print(format(i[0], '.2f'), i[1])
