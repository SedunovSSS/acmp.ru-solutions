def transpose_matrix(matrix):
    new_matrix = []
    for j in range(len(matrix[0])):
        temp = []
        for i in matrix:
            temp.append(i[j])

        new_matrix.append(temp)
    return new_matrix


def check(n, sudoku):
    for i in sudoku:
        for j in i:
            if j < 1 or j > n**2:
                return 'Incorrect'

    transpose_sudoku = transpose_matrix(sudoku)
    for i in range(n**2):
        if len(set(sudoku[i])) < len(sudoku[i]):
            return 'Incorrect'
        if len(set(transpose_sudoku[i])) < len(transpose_sudoku[i]):
            return 'Incorrect'
        
    sudoku_sqrs = []

    for i in range(0, n**2, n):
        for j in range(0, n**2, n):
            submatrix = []
            for k in range(n):
                submatrix += sudoku[i+k][j:j+n]
            sudoku_sqrs.append(submatrix)

    for i in sudoku_sqrs:
        if len(set(i)) < len(i) and sum(i) != n**2:
            return 'Incorrect'
    
    return 'Correct'


n = int(input())
sudoku = [list(map(int, input().split())) for _ in range(n**2)]
print(check(n, sudoku))
