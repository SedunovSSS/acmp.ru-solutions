a, b, c, d = [int(input()) for _ in range(4)]
values = [a, b, c, d]
values.sort()
print(values[0]*values[1] + values[2] * values[3])
