n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
profite_nums = [i for i in nums if i > 0]

nn = len(profite_nums)
max_sum = 0

for mm in range(1, m+1):
    _sum = sum(profite_nums[nn-mm:nn])
    max_sum = max(_sum, max_sum)

print(max_sum)
