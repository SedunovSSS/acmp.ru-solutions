num = input()

result = 0

for i in num:
    if i in '609':
        result += 1
    if i == '8':
        result += 2
print(result)
