def isPretty(n):
    _sum = sum(map(int, list(str(n))))
    _len = len(str(n))
    return True if _sum % _len == 0 else False


n = int(input())

num = 0
nums = []

while len(nums) < n+1:
    if isPretty(num):
        nums.append(num)
    num += 1

print(nums[n])
