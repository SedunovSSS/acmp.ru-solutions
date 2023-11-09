n = int(input())
for _ in range(n):
    num1, num2 = input().split()
    print('YES' if sorted(list(set(num1))) == sorted(list(set(num2))) else 'NO')
