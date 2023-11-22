n = int(input())
nums = list(map(int, input().split()))
indexes_big = []
indexes_small = []
max_sum_big = 0
max_sum_small = 0

if not any(nums):
    print(0)
else:
    for j, i in enumerate(nums):
        if i > 0:
            max_sum_big += i
            indexes_big.append(j+1)
        elif i < 0:
            max_sum_small += abs(i)
            indexes_small.append(j+1)

    if max_sum_big >= max_sum_small:
        print(len(indexes_big))
        print(*indexes_big)
    else:
        print(len(indexes_small))
        print(*indexes_small)
