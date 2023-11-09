def amber(a,b): 
    sum = 0 
    while a != 0: 
        sum += a % b 
        a //= b 
    return sum 

a1, b1 = map(int,input().split()) 
a2, b2 = map(int,input().split()) 

if amber(a1, b1) == amber(a2, b2):
    print(amber(a1, b1)) 
else: 
    print(0)