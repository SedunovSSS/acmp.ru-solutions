n = int(input())
nums = []

i = 1
while len(nums)-1 < n:
    if not len(set(str(i))) < len(str(i)):
        nums.append(i)
    i += 1

print(nums[n-1])
