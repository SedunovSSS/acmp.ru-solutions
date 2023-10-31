a, b = map(int, input().split())
 
if a == 0 and b == 0:
    result_min = 0
    result_max = 0
else:
    if a == 0:
        result = "Impossible"
    else:
        if b == 0:
            result_min = a
            result_max = a
        else:
            if b <= a:
                result_min = a
                result_max = a + b - 1
            else:
                result_min = b
                result_max = a + b - 1
if a == 0 and b != 0:
    result = "Impossible"
else:
   result = str(str(result_min) + " " + str(result_max))

print(result)
