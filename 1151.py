def check(pswrd):
    find_upper, find_lower, find_digit = False, False, False
    if len(pswrd) < 12:
        return 'No'
    for i in pswrd:
        if i.isascii():
            if i.isupper() and not find_upper:
                find_upper = True
                continue
            if i.islower() and not find_lower:
                find_lower = True
                continue
        if i.isdigit() and not find_digit: 
            find_digit = True
            continue
    return 'Yes' if find_upper and find_lower and find_digit else 'No'

pswrd = input()
print(check(pswrd))