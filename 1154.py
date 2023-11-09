ip_map = map(int, input().split("."))
ip = []
result = None
try:
    [ip.append(int(i)) for i in ip_map]
except:
    result = "Bad"
 
if result == None:
    for i in ip:
        if i > 255 or i < 0:
            result = "Bad"
            break
        else:
            result = "Good"
 
 
print(result)