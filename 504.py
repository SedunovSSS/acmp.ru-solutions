K = int(input())

flowers = ['G', 'C', 'V']

for i in range(K):
    flowers[1], flowers[2] = flowers[2], flowers[1]
    flowers[0], flowers[1] = flowers[1], flowers[0]

print(f"{flowers[0]}{flowers[1]}{flowers[2]}")