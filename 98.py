n = int(input())
xz = list(map(int, input().split()))
xz2 = [0, 0]
for i in range(n):
	if xz[0] >= xz[-1]:
		xz2[i%2] += xz[0]
		xz.pop(0)
	else:
		xz2[i%2] += xz[-1]
		xz.pop(-1)
print(f'{xz2[0]}:{xz2[1]}')