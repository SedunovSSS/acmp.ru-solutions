def transpose_matrix(matrix):
    new_matrix = []

    for j in range(len(matrix[0])):
        temp = []
        for i in matrix:
            temp.append(i[j])

        new_matrix.append(temp)
    
    return new_matrix


def get_matrix_diagonals(matrix):
    diagonal_1 = []
    diagonal_2 = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                diagonal_1.append(matrix[i][j])

    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[0])):
            if i+j == len(matrix[i])-1:
                diagonal_2.append(matrix[i][j])

    return diagonal_1, diagonal_2

crossWin, nullWin, nobody = False, False, False

cross = 'X'
null = 'O'
empty = '.'

m = [list(input()) for _ in range(3)]

tr_map = transpose_matrix(m)

for i in range(3):
    setted_map = set(m[i])
    if empty not in m[i]:
        if len(setted_map) == 1:
            if cross in m[i]:
                crossWin = True
            if null in m[i]:
                nullWin = True
    setted_tr_map = set(tr_map[i])
    if empty not in tr_map[i]:
        if len(setted_tr_map) == 1:
            if cross in tr_map[i]:
                crossWin = True
            if null in tr_map[i]:
                nullWin = True

diagonal_1, diagonal_2 = get_matrix_diagonals(m)

setted_d1 = set(diagonal_1)
setted_d2 = set(diagonal_2)

if len(setted_d1) == 1:
    if cross in diagonal_1:
        crossWin = True
    if null in diagonal_1:
        nullWin = True
if len(setted_d2) == 1:
    if cross in diagonal_2:
        crossWin = True
    if null in diagonal_2:
        nullWin = True

if not crossWin and not nullWin and not any(empty in i for i in m):
    nobody = True

print('Draw') if nobody else print('Win') if crossWin else print('Lose')
