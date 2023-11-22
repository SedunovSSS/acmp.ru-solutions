h, m = map(int, input().split(':'))

while True:
    m += 1
    if m % 60 == 0:
        m = 0
        h += 1
        if h % 24 == 0:
            h, m = 0, 0
    str_h, str_m = '0'+str(h) if h < 10 else str(h), '0'+str(m) if m < 10 else str(m)
    if str_h == str_m[::-1]:
        print(str_h+':'+str_m)
        break
    
