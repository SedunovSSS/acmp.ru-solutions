def get_sum(n):
    h = n // 100
    return (n - ((h << 6) + (h << 5) + (h << 2))) // 10 + h


n = int(input())
xuys = [input() for _ in range(n)]

for number_line in xuys:
    first_number = int(number_line[0]) + int(number_line[1]) + int(number_line[2])
    second_number = int(number_line[3:])
    last = int(number_line[5])
    increment = get_sum(second_number + 1)
    decrement = get_sum(second_number - 1)
    if last != 9:
        increment += last + 1
    if last == 0:
        decrement += 9
    else:
        decrement += last - 1
    if first_number == increment or first_number == decrement:
        print("Yes")
    else:
        print("No")