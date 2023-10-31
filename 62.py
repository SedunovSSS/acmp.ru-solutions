numbers = ['1', '2', '3', '4', '5', '6', '7', '8']
symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

a, b = list(input())

a_ind, b_ind = symbols.index(a)+1, numbers.index(b)+1

if a_ind % 2 == 0 and b_ind % 2 == 0:
    print('BLACK')
elif a_ind % 2 != 0 and b_ind % 2 != 0:
    print('BLACK')
else:
    print('WHITE')