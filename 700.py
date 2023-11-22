n, v, k = map(int, input().split())
result = 0
if n*k < v+k:
    s = 'YES' 
else:
    s = 'NO'
for i in range(n):
	result += v
	v -= k
	if v <= 0:
		break
print(s, result)