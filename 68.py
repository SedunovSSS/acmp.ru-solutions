place = input()
trips = int(input())

if trips % 2 == 0 and place != 'Home':
    print('No')
else:
    print('Yes')
