a = int(input())
b = input().split()
chetn = ""
nechetn = ""
for i in b:
    if int(i) % 2 == 0:
        chetn+=i+" "
    else:
        nechetn+=i+" "

print(nechetn)
print(chetn)
if len(chetn) >= len(nechetn):
    print("YES")
else:
    print("NO")