string1, string2 = input(), input()
unique1, unique2 = sorted(list(set(string1))), sorted(list(set(string2)))
if len(unique1) == len(unique2):
    for f, s in zip(unique1, unique2):
        if f != s or string1.count(f) != string2.count(s):
            print('NO')
            break
    else:
        print('YES')
else:
    print('NO')