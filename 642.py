n, s = map(int, input().split())
nums = sorted(list(map(int, input().split())))
_sum, k = 0, 0
for i in range(n):
    if _sum + nums[i] <= s:
        _sum += nums[i]
        k += 1
print(k)