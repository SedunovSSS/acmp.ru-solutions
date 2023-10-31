m = [[j+i for j in range(0, 8)] for i in range(1, 65, 8)]

num = int(input())

cord_i = 0
cord_j = 0

for index, i in enumerate(m):
    if num in i:
        cord_i = index
        cord_j = i.index(num)

if cord_i == cord_j == 0:
    cords = [m[cord_i+1][cord_j], m[cord_i][cord_j+1]]
elif cord_i == cord_j == len(m)-1:
    cords = [m[cord_i-1][cord_j], m[cord_i][cord_j-1]]
elif cord_i == len(m)-1 and cord_j == 0:
    cords = [m[cord_i-1][cord_j], m[cord_i][cord_j+1]]
elif cord_i == 0 and cord_j == len(m)-1:
    cords = [m[cord_i+1][cord_j], m[cord_i][cord_j-1]]
elif cord_i == 0 and 0 < cord_j < len(m)-1:
    cords = [m[cord_i][cord_j-1], m[cord_i][cord_j+1], m[cord_i+1][cord_j]]
elif cord_i == len(m)-1 and 0 < cord_j < len(m)-1:
    cords = [m[cord_i][cord_j-1], m[cord_i][cord_j+1], m[cord_i-1][cord_j]]
elif cord_j == 0 and 0 < cord_i < len(m)-1:
    cords = [m[cord_i-1][cord_j], m[cord_i+1][cord_j], m[cord_i][cord_j+1]]
elif cord_j == len(m)-1 and 0 < cord_i < len(m)-1:
    cords = [m[cord_i-1][cord_j], m[cord_i+1][cord_j], m[cord_i][cord_j-1]]
else:
    cords = [m[cord_i-1][cord_j], m[cord_i+1][cord_j], m[cord_i][cord_j-1], m[cord_i][cord_j+1]]

cords = list(sorted(cords))
print(*cords)