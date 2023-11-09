def isPrime(num):
    k = 2
    while k**2 <= num and num % k != 0:
        k+=1
    return k**2 > num

m, n = map(int, input().split())

nums = [i for i in range(m, n+1) if isPrime(i)]
if len(nums) == 0:
    print('Absent')
else:
    for i in nums:
        print(i)