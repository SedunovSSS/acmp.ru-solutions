def check(matrix):
    for i in range(3):
        for j in range(3):
            sub = []
            for x in range(i, i + 2):
                for y in range(j, j + 2):
                    sub.append(matrix[x][y])
            if len(list(set(sub))) == 1:
                return 'No'
    return 'Yes'


matrix = [input() for _ in range(4)]
print(check(matrix))