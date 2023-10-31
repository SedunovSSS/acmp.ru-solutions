a, b = input().split()

bull = 0
cow = 0

for i in range(4):
    for j in range(4):
        if a[i] == b[j]:
            if i == j:
                bull += 1
            else:
                cow += 1

print(bull, cow)