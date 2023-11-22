string = input()
result = ''
digit = ''

ceil = lambda x: int(x) if x == int(x) else int(x)+1

for i in string:
    if i.isdigit():
        digit += i
    else:
        digit_int = 1 if digit == '' else int(digit)
        digit = ''
        result += i * digit_int

for i in range(ceil(len(result)/40)):
    print(result[i*40:(i+1)*40] if i < ceil(len(result)//40) else result[i*40:])