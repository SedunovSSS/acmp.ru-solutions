n = int(input())

list_ = list(map(int, list(str(n))))

a = list(sorted(list_))
b = list(reversed(a))

a_temp = [i for i in a if i != 0]
min_index = a.index(min(a_temp))    

a[0], a[min_index] = a[min_index], a[0]

a, b = list(map(str, a)), list(map(str, b))

print(''.join(a), ''.join(b))
