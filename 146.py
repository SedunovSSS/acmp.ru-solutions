s = input()
n = int(s)
a = int('1' + '0'*((len(s) +1 ) // 2))
next = a - 1
while next < a:
    a = next
    next = (a + n // a) // 2
print(a)
