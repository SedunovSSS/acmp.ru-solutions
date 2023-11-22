a, b, c = map(int, input().split())
result = ''
if a != 0:
    result += '1' if a == 1 else str(a)
if b != 0:
    if b == 1 or b == -1:
        result += '-x' if b < 0 else 'x' if result == '' else '+x'
    else:
        result += str(b)+'x' if b < 0 or result == '' else '+' + str(b)+'x'
if c != 0:
    if c == 1 or c == -1:
        result += '-y' if c < 0 else 'y' if result == '' else '+y'
    else:
        result += str(c)+'y' if c < 0 or result == '' else '+' + str(c)+'y'


result = '0' if result == '' else result
print(result)
