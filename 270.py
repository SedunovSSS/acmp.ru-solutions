def check(string):
    isJavaVar = False
    result = ''
    ascii_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lower = ascii_upper.lower()

    for i in ascii_upper:
        if i in string:
            isJavaVar = True
            break

    if (isJavaVar and '_' in string) or (string[0] not in ascii_lower + ascii_upper):
        return 'Error!'
    
    if isJavaVar:
        for i in string:
            if i in ascii_upper:
                result += ('_' + i.lower())
            else:
                result += i
    else:
        words = string.split('_')
        if '' in words:
            return 'Error!'
        result += words[0]
        for i in words[1:]:
            word = i[0].upper() + i[1:]
            result += word

    if result[0] == '_':
        return 'Error!'

    return result


string = input()
print(check(string))