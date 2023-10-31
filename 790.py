def convert_to(number, base, upper=True):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result


d, m, y = map(int, input().split('/'))
d, m, y = convert_to(d, d+1), convert_to(m, d+1), convert_to(y, d+1)
print(f'{d}/{m}/{y}')
