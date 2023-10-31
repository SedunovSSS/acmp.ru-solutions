n = input()

sum_even = 0
sum_odd = 0

for i in range(len(n)):
    if i % 2 == 1:
        sum_even += int(n[i])
    else:
        sum_odd += int(n[i])

ans = sum_even - sum_odd
print('YES' if ans % 11 == 0 else 'NO')