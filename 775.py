n, m = input().split()

if m == "0":
    print('NO')
else:
    print(n[:len(n)-1] + str(int(n[len(n)-1])+1))
