a = int(input())
count = 0
for i in range(a+1):
    if i != 0 and a % i == 0:
        count+=i
print(count)