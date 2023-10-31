a = int(input())
glist = [int(input()) for i in range(a)]
null, one = [], []
for i in glist:
    if i == 1:
        one.append(i)
    else:
        null.append(i)
if len(one) > len(null):
    print(len(null))
else:
    print(len(one))