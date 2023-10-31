num, word = input().split()
num = int(num)
print(word[0:num-1] + word[num:len(word)])