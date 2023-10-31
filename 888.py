n = int(input())
accepteds = list(map(int, input().split()))
pos = 0
ball = 3

for a in accepteds:
    if bool(a):
        pos += ball
        ball += 1
    else:
        ball = max(ball-3, 3)
print(pos)
