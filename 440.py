shuts = [0]*5

for i in range(5):
	x, y = map(int, input().split())
	for j in range(5):
		if (x-25*j)**2+y**2 <= 100:
			shuts[j] = 1
			break
			
print(sum(shuts))
