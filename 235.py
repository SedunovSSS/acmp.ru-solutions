commands = input()
x, y = 0, 0
move = 0
moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
steps = [(x, y)]
result = -1
step = 0
pos = 0

for i in commands:
    dx, dy = moves[move]
    if i == 'S':
        x, y = x+dx, y+dy
        step += 1
        if (x, y) in steps:
            result = step
            break
        steps.append((x, y))
    if i == 'R':
        pos += 1
        move = pos % 4
    if i == 'L':
        pos -= 1
        move = pos % 4

print(result)    
