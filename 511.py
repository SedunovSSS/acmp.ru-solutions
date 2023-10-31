n = int(input())
time = (n-1)*5

if time > 720:
    print('NO')
else:
    print(time//60, time%60)