def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


m = int(input())
nums = list(map(int, input().split()))

max_nums = max(nums)
prime_nums = ''

i = 2

while len(prime_nums) < max_nums:
    if isPrime(i):
        prime_nums += str(i)
    i += 1

result = ''
for i in nums:
    result += prime_nums[i-1]

print(result)