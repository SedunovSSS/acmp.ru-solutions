n, m = map(int, input().split())
nums = [0]*10
for i in range(1, n+1): 
    for j in range(1, m+1):
        multiply = i*j
        while multiply > 0:
            nums[multiply % 10] += 1
            multiply = multiply // 10

print(*nums, sep='\n')
