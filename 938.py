def isPrime(num):
    k = 2
    while k**2 <= num and num % k != 0:
        k+=1
    return k**2 > num

all_simple_nums = [i for i in range(2, 1025) if isPrime(i)]

n = int(input())
values = list(map(int, input().split()))

result = 0
max_count = 0

for i in values:
    num = 2
    count = 0
    while num <= i:
        if num in all_simple_nums:
            if i / num == int(i / num):
                count += 1
        num += 1
    if max_count < count:
        max_count = count
        result = i
    if max_count == count:
        if i < result:
            result = i

print(result)