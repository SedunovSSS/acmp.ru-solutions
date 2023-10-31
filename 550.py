year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    if len(str(year)) == 1:
        print(f'12/09/000{year}')
    elif len(str(year)) == 2:
        print(f'12/09/00{year}')
    elif len(str(year)) == 3:
        print(f'12/09/0{year}')
    else:
        print(f'12/09/{year}')
else:
    if len(str(year)) == 1:
        print(f'13/09/000{year}')
    elif len(str(year)) == 2:
        print(f'13/09/00{year}')
    elif len(str(year)) == 3:
        print(f'13/09/0{year}')
    else:
        print(f'13/09/{year}')