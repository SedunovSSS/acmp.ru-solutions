import sys 
sys.set_int_max_str_digits(0)

n = int(input())

d = 1
if n > 9:
    for i in range(len(list(str(n)))):
        if n % d == 0:
            res = d
            d = d * 10
else:
    res = 1

print(res)