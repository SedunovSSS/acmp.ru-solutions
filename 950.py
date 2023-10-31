ascii = 'abcdefghijklmnopqrstuvwxyz'
string = input()

nulls_count = 0
result = ''

for i in string:
    if i == '1':
        result += ascii[nulls_count]
        nulls_count = 0
    else:
        nulls_count += 1

print(result)
