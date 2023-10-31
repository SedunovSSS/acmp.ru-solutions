string = input()
strs = ['>>-->', '<--<<']
result = 0

for i in range(0, len(string)):
    if string[i:i+5] in strs:
        result += 1

print(result)