value = input()
x_index = value.index('x')

if x_index == 0:
    x = int(value[4])-int(value[1:3])
elif x_index == 2:
    x = int(value[0])-int(value[4]) if value[1]=='-' else int(value[4])-int(value[0])
else:
    x = int(value[0])+int(value[1:3])

print(x)