a1, b1, c1 = list(sorted(map(int, input().split())))
a2, b2, c2 = list(sorted(map(int, input().split())))

if (a1,b1,c1) == (a2,b2,c2):
    print('Boxes are equal')
elif a1 >= a2 and b1 >= b2 and c1 >= c2:
    print('The first box is larger than the second one')
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    print('The first box is smaller than the second one')
else:
    print('Boxes are incomparable')