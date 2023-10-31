f1, s1 = map(int, input().split())
f2, s2 = map(int, input().split())
f3, s3 = map(int, input().split())
f4, s4 = map(int, input().split())

if sum([f1, f2, f3, f4]) == sum([s1, s2, s3, s4]):
    print('DRAW')
if sum([f1, f2, f3, f4]) > sum([s1, s2, s3, s4]):
    print(1)
if sum([f1, f2, f3, f4]) < sum([s1, s2, s3, s4]):
    print(2)
