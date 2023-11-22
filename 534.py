n = int(input())
presses = list(map(int, input().split()))
k = int(input())
keys = list(map(int, input().split()))

for i in range(n):
    if presses[i] >= keys.count(i+1):
        print('no')
    else:
        print('yes')
