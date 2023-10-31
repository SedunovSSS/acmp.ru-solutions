a = int(input())
count = 0
a = bin(a)
for i in a:
    if i == "1":
        count+=1
print(count)