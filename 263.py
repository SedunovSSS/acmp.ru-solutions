n, i, j = map(int, input().split())

count_1 = abs(i - j) - 1 
count_2 = n - abs(i - j) - 1 

print(min(count_1, count_2))